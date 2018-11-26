import logging

import docker


class DockerPyWrapper:
    RECOGNISED_FIXTURE = 'dockerpy'

    def __init__(self):
        self._client = docker.from_env()

    def ls_images(self):
        image_tags = []
        for image in self._client.images.list():
            for tag in image.tags:
                image_tags.append(tag)
        return image_tags

    def rm_images(self, images_to_rm):
        for image_to_rm in images_to_rm:
            self._rm_image(image_to_rm)

    def _rm_image(self, image_to_rm):
        if image_to_rm in self.ls_images():
            logging.debug(image_to_rm)
            self._client.images.remove(image_to_rm, force=True)

    def pull(self, images_to_pull):
        for image_to_pull in images_to_pull:
            if image_to_pull not in self.ls_images():
                logging.debug(image_to_pull)
                try:
                    self._client.images.pull(image_to_pull)
                except docker.errors.ImageNotFound as exception:
                    logging.error(str(exception))
                    return False
            else:
                logging.debug('skipped: %s', image_to_pull)
        return True

    def ls_containers(self, images_from_config):
        containers = []
        for container in self._client.containers.list():
            for tag in container.image.tags:
                for image_from_config in images_from_config:
                    if image_from_config == tag:
                        containers.append({'image': tag,
                                           'id': container.id,
                                           'container': container})
        return containers

    def start_containers(self, config):
        self.rm_containers(config.images())
        for container in config.containers():
            self._start_container(config, container)

    def _start_container(self, config, container):
        try:
            logging.debug(container['image'])

            try:
                self._start_network(config, container['network'])
            except KeyError:
                pass

            detached_container = self._client.containers.run(container['image'],
                                                             ** config.container_kwargs(container),
                                                             detach=True)
            logging.debug(detached_container.attrs['Id'])
        except KeyError:
            logging.error('missing: image')
            pass

    def rm_containers(self, containers_to_stop):
        for docker_container in self.ls_containers(containers_to_stop):
            for container_to_stop in containers_to_stop:
                if docker_container['image'] == container_to_stop:
                    self._rm_container_artefacts(docker_container)

        self._client.containers.prune()
        self._client.networks.prune()

    def _rm_container_artefacts(self, docker_container):
        logging.debug(docker_container['id'])
        try:
            docker_container['container'].stop(timeout=1)
            docker_container['container'].remove(force=True)
        except docker.errors.NotFound:
            pass
        self._client.volumes.prune()

    def ls_networks(self, config_networks):
        networks = []
        for network in self._client.networks.list():
            for config_network in config_networks:
                if config_network == network.name:
                    logging.debug(network.name)
                    networks.append(network.name)
        return networks

    def _start_network(self, config, network_to_start):
        if network_to_start not in self.ls_networks(config.networks()):
            logging.debug('%s', network_to_start)
            self._client.networks.create(network_to_start)

    def ls_volumes(self, config_volumes):
        self._client.volumes.prune()
        volumes = []
        for volume in self._client.volumes.list():
            for config_volume in config_volumes:
                if volume.name in config_volume:
                    logging.debug(config_volume)
                    volumes.append(config_volume)
        return sorted(volumes)

import logging


class Config:
    def __init__(self, configuration_from_fixture):
        self._configuration_from_fixture = configuration_from_fixture

    def images(self):
        images = []
        for configuration in self._configuration_from_fixture:
            try:
                images.append(configuration['image'])
            except KeyError:
                logging.error('missing: image')
        return sorted(images)

    def containers(self):
        return self._configuration_from_fixture

    def networks(self):
        networks = []
        for configuration in self._configuration_from_fixture:
            try:
                if configuration['network'] not in networks:
                    networks.append(configuration['network'])
            except KeyError:
                pass
        return sorted(networks)

    def volumes(self):
        volumes = []
        for configuration in self._configuration_from_fixture:
            try:
                for image_volume in configuration['volumes']:
                    if image_volume not in volumes:
                        volumes.append(image_volume)
            except KeyError:
                pass
        return sorted(volumes)

    def container_kwargs(self, container):
        container_dict = {}

        Config._container_kwarg(container_dict, container, 'name')
        Config._container_kwarg(container_dict, container, 'ports')
        Config._container_kwarg(container_dict, container, 'network')
        Config._container_kwarg(container_dict, container, 'volumes')
        Config._container_kwarg(container_dict, container, 'command')
        Config._container_kwarg(container_dict, container, 'environment')

        return container_dict

    @classmethod
    def _container_kwarg(cls, container_dict, container, key):
        try:
            container_dict[key] = container[key]
        except KeyError:
            logging.warning('%s - missing: %s' % (container['image'], key))
        return container_dict


class ConfigException(Exception):
    pass

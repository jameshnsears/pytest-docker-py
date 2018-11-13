import docker


class DockerPyWrapper:
    def images_to_pull(self, required_images=[]):
        images_to_pull = []
        for required_image in required_images:
            if required_image not in DockerPyWrapper._local_images():
                images_to_pull.append(required_image)

        if not images_to_pull:
            return None
        else:
            return images_to_pull

    @staticmethod
    def _local_images():
        local_image_tags = []
        for local_image in docker.from_env().images.list():
            for local_image_tag in local_image.tags:
                local_image_tags.append(local_image_tag)
        return local_image_tags

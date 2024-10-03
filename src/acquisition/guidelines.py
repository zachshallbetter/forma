class Guidelines:
    @staticmethod
    def print_guidelines():
        message = """
        Image Acquisition Guidelines:
        - Use a high-resolution camera for better accuracy.
        - Ensure even lighting to avoid shadows and reflections.
        - Capture images from multiple angles, covering all sides of the limb.
        - Maintain consistent distance from the limb in all images.
        - Use a neutral background to enhance segmentation.
        - Include a reference object or scale marker in some images.
        """
        print(message)

    @staticmethod
    def save_guidelines(filename):
        with open(filename, 'w') as f:
            f.write(Guidelines.get_guidelines())
        print(f"Guidelines saved to {filename}")

    @staticmethod
    def get_guidelines():
        return Guidelines.print_guidelines.__func__.__globals__['message']

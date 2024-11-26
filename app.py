# Base class: Smartphone
class Smartphone:
    def __init__(self, brand, model, storage, battery_life):
        # Attributes
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.battery_life = battery_life  # in hours
    
    # Method to display phone details
    def display_details(self):
        return f"{self.brand} {self.model} - Storage: {self.storage}GB, Battery: {self.battery_life} hours"
    
    # Method to check battery status
    def check_battery(self):
        return f"{self.model} has {self.battery_life} hours of battery life remaining."


# Subclass: CameraSmartphone
class CameraSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery_life, camera_resolution, optical_zoom):
        # Initialize the base class
        super().__init__(brand, model, storage, battery_life)
        # New attributes for camera phones
        self.camera_resolution = camera_resolution  # in MP (megapixels)
        self.optical_zoom = optical_zoom  # zoom level
    
    # Method specific to CameraSmartphone
    def take_photo(self):
        return f"{self.model} takes a photo with {self.camera_resolution}MP resolution and {self.optical_zoom}x optical zoom!"

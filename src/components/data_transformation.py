class DataTransformationConfig:
    def __init__(self):
        self.some_config = "default_value"

class DataTransformation:
    def __init__(self):
        print("Data Transformation Initialized")

    def initiate_data_transformation(self, train_data, test_data):
        return train_data, test_data, None

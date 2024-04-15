# Replace this URL with your actual API endpoint for image analysis
# apiKey = 'AIzaSyCYPudaw-RCuR85r1Np3Y4KvYJf0KgJfTM'
api_url = 'https://vision.googleapis.com/v1/images:annotate?key=AIzaSyCYPudaw-RCuR85r1Np3Y4KvYJf0KgJfTM'

import tkinter as tk
from tkinter import filedialog
import requests
import base64

class ImageAnalysisApp:
    def __init__(self, root):
        """
        Initialize the Image Analysis application.
        
        Parameters:
            root (tk.Tk): The root window of the application.
        """
    
        self.root = root
        self.image_path = None
        self.detected_labels = []
        self.safe_search_results = {}

        #setup the UI elements:
        self.root.title("Image Analysis")
        self.root.geometry("800x600")
        self.root.config(bg="#062775")

        # Title Label
        self.title_label = tk.Label(self.root, text="Image Analysis", font=("Arial", 24), bg="#333", fg="white", padx=10, pady=10)
        self.title_label.pack(fill=tk.X)

        # Image Label
        self.image_label = tk.Label(self.root, text="No Image Selected", font=("Arial", 12), bg="#030a1a", padx=10, pady=10)
        self.image_label.pack()

        # Pick Button
        self.pick_button = tk.Button(self.root, text="Select an Image", command=self.pick_and_analyze_image)
        self.pick_button.pack(pady=10)

        # Detected Labels Label
        self.detected_labels_label = tk.Label(self.root, text="Detected Labels:", font=("Arial", 16), bg="#030a1a", padx=10, pady=10)
        self.detected_labels_label.pack(pady=5)

        # Detected Labels Listbox
        self.detected_labels_listbox = tk.Listbox(self.root, width=40, height=10, font=("Arial", 12))
        self.detected_labels_listbox.pack()

        # Safe Search Label
        self.safe_search_label = tk.Label(self.root, text="Safe Search Detection:", font=("Arial", 16), bg="#030a1a", padx=10, pady=10)
        self.safe_search_label.pack(pady=5)

        # Safe Search Listbox
        self.safe_search_listbox = tk.Listbox(self.root, width=40, height=10, font=("Arial", 12))
        self.safe_search_listbox.pack()

    #Define methods for picking and analyzing images:
    def pick_and_analyze_image(self):
        """
        Open file dialog to pick an image and analyze it.
        """
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image_path = file_path
            self.image_label.config(text="Selected Image: " + self.image_path)
            self.analyze_image()

    def analyze_image(self):
        """
        Analyze the selected image using the image analysis API.
        """
        if not self.image_path:
            print("Please provide an image")
            return

        try:
            with open(self.image_path, "rb") as image_file:
                encoded_image = base64.b64encode(image_file.read()).decode("utf-8")
            
            payload = {
                "requests": [
                    {
                        "image": {"content": encoded_image},
                        "features": [{"type": "LABEL_DETECTION"}, {"type": "SAFE_SEARCH_DETECTION"}]
                    }
                ]
            }

            # Send the API request to your image analysis server or API
            response = requests.post(api_url, json=payload)

            if response.status_code == 200:
                data = response.json()
                self.process_analysis_results(data)
            else:
                print(f"Failed to analyze image. Status code: {response.status_code}")
        except Exception as e:
            print(f"Error analyzing image: {e}")

    def process_analysis_results(self, data):
        """
        Process the results from the image analysis API and update the GUI.

        Parameters:
            data (dict): The response data from the image analysis API.
        """
        self.detected_labels_listbox.delete(0, tk.END)
        self.safe_search_listbox.delete(0, tk.END)

        if "labelAnnotations" in data["responses"][0]:
            self.detected_labels = data["responses"][0]["labelAnnotations"]
            for label in self.detected_labels:
                label_name = label["description"]
                label_confidence = label["score"] * 100
                self.detected_labels_listbox.insert(tk.END, f"{label_name}: {label_confidence:.2f}%")

        if "safeSearchAnnotation" in data["responses"][0]:
            self.safe_search_results = data["responses"][0]["safeSearchAnnotation"]
            for category, likelihood in self.safe_search_results.items():
                likelihood_string = self.get_likelihood_string(likelihood)
                likelihood_confidence = self.get_likelihood_confidence(likelihood)
                self.safe_search_listbox.insert(tk.END, f"{category.capitalize()}: {likelihood_string} {likelihood_confidence:.2f}%")

    @staticmethod
    def get_likelihood_string(likelihood_value):
        """
        Get the likelihood string based on the likelihood value.

        Parameters:
            likelihood_value (str): The likelihood value.

        Returns:
            str: The corresponding likelihood string.
        """
        likelihood_mapping = {
            "VERY_LIKELY": "Very Likely",
            "LIKELY": "Likely",
            "POSSIBLE": "Possible",
            "UNLIKELY": "Unlikely",
            "VERY_UNLIKELY": "Very Unlikely"
        }
        return likelihood_mapping.get(likelihood_value, "Unknown")

    @staticmethod
    def get_likelihood_confidence(likelihood_value):
        """
        Get the confidence value based on the likelihood value.

        Parameters:
            likelihood_value (str): The likelihood value.

        Returns:
            float: The corresponding confidence value.
        """
        confidence_mapping = {
            "VERY_LIKELY": 0.9,
            "LIKELY": 0.75,
            "POSSIBLE": 0.5,
            "UNLIKELY": 0.25,
            "VERY_UNLIKELY": 0.1
        }
        return confidence_mapping.get(likelihood_value, 0.0) * 100


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageAnalysisApp(root)
    root.mainloop()

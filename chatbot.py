import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.metrics import jaccard_distance

class SimpleChatbot:
    def __init__(self):
        self.responses = {
            "hello": "Hello! How can I help you?",
            "hi": "Hi there!",
            "how are you": "I'm doing well, thank you!",
            "bye": "Goodbye!",
            "default": "I'm sorry, I don't understand. Can you please rephrase?",
        }
        self.stop_words = set(stopwords.words("english"))

    def preprocess_input(self, text):
        # Tokenize and remove stop words
        tokens = word_tokenize(text.lower())
        filtered_tokens = [token for token in tokens if token not in self.stop_words]
        return " ".join(filtered_tokens)

    def get_response(self, user_input):
        processed_input = self.preprocess_input(user_input)
        best_similarity = 0
        best_response = ""

        for key, value in self.responses.items():
            processed_key = self.preprocess_input(key)
            similarity = 1 - jaccard_distance(set(processed_key.split()), set(processed_input.split()))

            if similarity > best_similarity:
                best_similarity = similarity
                best_response = value

        return best_response

    def start_chat(self):
        print("Chatbot: Hello! How can I assist you?")

        while True:
            user_input = input("You: ").lower()

            if user_input == "bye":
                print("Chatbot: Goodbye!")
                break

            response = self.get_response(user_input)
            print("Chatbot:", response)

if __name__ == "__main__":
    nltk.download("punkt")
    nltk.download("stopwords")
    
    chatbot = SimpleChatbot()
    chatbot.start_chat()

import random

class Magic8Ball:
    """A simple Magic 8 Ball implementation."""
    
    # Positive responses
    POSITIVE_RESPONSES = [
        "It is certain",
        "It is decidedly so",
        "Without a doubt",
        "Yes definitely",
        "You may rely on it",
        "As I see it, yes",
        "Most likely",
        "Outlook good",
        "Yes",
        "Signs point to yes",
    ]
    
    # Non-committal responses
    NONCOMMITTAL_RESPONSES = [
        "Reply hazy, try again",
        "Ask again later",
        "Better not tell you now",
        "Cannot predict now",
        "Concentrate and ask again",
    ]
    
    # Negative responses
    NEGATIVE_RESPONSES = [
        "Don't count on it",
        "My reply is no",
        "My sources say no",
        "Outlook not so good",
        "Very doubtful",
        "Don't even think about it",
        "Absolutely not",
        "No way",
        "No",
        "Definitely not",
    ]
    
    def __init__(self):
        """Initialize the Magic 8 Ball with all responses."""
        self.all_responses = (
            self.POSITIVE_RESPONSES +
            self.NONCOMMITTAL_RESPONSES +
            self.NEGATIVE_RESPONSES
        )
    
    def ask(self, question: str) -> str:
        """
        Ask the Magic 8 Ball a question and get a response.
        
        Args:
            question: The question to ask the Magic 8 Ball
            
        Returns:
            A random response from the Magic 8 Ball
        """
        if not question or not question.strip():
            return "Please ask a question!"
        
        return random.choice(self.all_responses)


if __name__ == "__main__":
    # Example usage
    ball = Magic8Ball()
    
    questions = [
        "Will I be successful?",
        "Should I go to the party?",
        "Is it a good day?",
    ]
    
    for question in questions:
        response = ball.ask(question)
        print(f"Q: {question}")
        print(f"A: {response}\n")

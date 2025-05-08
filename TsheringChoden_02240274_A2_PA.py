import random

# Class: Guess the Number Game
class GuessNumberGame:
    def __init__(self):
        self.number_to_guess = random.randint(1, 100)
        self.guess_count = 0

    def play(self):
        print("Welcome to the Guess the Number Game!")
        while True:
            try:
                guess = int(input("Guess a number between 1 and 100: "))
                if 1 <= guess <= 100:
                    self.guess_count += 1
                    if guess < self.number_to_guess:
                        print("Too low!")
                    elif guess > self.number_to_guess:
                        print("Too high!")
                    else:
                        print(f"Correct! It took you {self.guess_count} guesses.")
                        return self.guess_count
                else:
                    print("Please guess a number between 1 and 100.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

# Class: Rock Paper Scissors Game
class RockPaperScissors:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]

    def play(self):
        print("Welcome to Rock, Paper, Scissors!")
        computer_choice = random.choice(self.choices)
        while True:
            user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
            if user_choice in self.choices:
                break
            else:
                print("Invalid choice. Please choose rock, paper, or scissors.")
        print(f"Computer chose {computer_choice}.")
        if user_choice == computer_choice:
            print("It's a draw!")
            return 0
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
            return 1
        else:
            print("You lose!")
            return -1

# Class: Trivia Pursuit Game
class TriviaPursuitQuiz:
    def __init__(self):
        self.questions = {
            "Science": [
                ("What is the chemical symbol for water?", ["H2O", "O2", "CO2", "H2"], "H2O"),
                ("What planet is known as the Red Planet?", ["Earth", "Mars", "Jupiter", "Saturn"], "Mars")
            ],
            "Geography": [
                ("Which is the largest ocean on Earth?", ["Atlantic", "Indian", "Arctic", "Pacific"], "Pacific"),
                ("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], "Paris")
            ]
        }

    def play(self):
        print("Welcome to Trivia Pursuit!")
        score = 0
        for category, questions_list in self.questions.items():
            print(f"\nCategory: {category}")
            for question, options, correct_answer in questions_list:
                print(f"\n{question}")
                for idx, option in enumerate(options, 1):
                    print(f"{idx}. {option}")
                while True:
                    try:
                        answer = int(input("Enter the number of your answer: "))
                        if 1 <= answer <= 4:
                            if options[answer - 1] == correct_answer:
                                print("Correct!")
                                score += 1
                            else:
                                print("Wrong answer!")
                            break
                        else:
                            print("Please enter a number between 1 and 4.")
                    except ValueError:
                        print("Invalid input. Please enter a number between 1 and 4.")
        print(f"\nYour final score is {score}.")
        return score

# Class: Pokemon Card Binder Manager
class PokemonCardBinder:
    def __init__(self):
        self.binder = []

    def add_pokemon_card(self):
        card_name = input("Enter the name of the Pokemon card: ")
        card_type = input("Enter the type of the card (e.g., Fire, Water): ")
        self.binder.append({"name": card_name, "type": card_type})
        print(f"{card_name} card added to the binder!")

    def reset_binder(self):
        self.binder.clear()
        print("The binder has been reset.")

    def view_current_placements(self):
        if self.binder:
            print("Current Pokemon Cards in Binder:")
            for card in self.binder:
                print(f"Name: {card['name']}, Type: {card['type']}")
        else:
            print("No cards in the binder yet.")

    def manage(self):
        print("Welcome to the Pokemon Card Binder Manager!")
        while True:
            print("\nMain Menu:")
            print("1. Add Pokemon card")
            print("2. Reset binder")
            print("3. View current placements")
            print("4. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_pokemon_card()
            elif choice == '2':
                self.reset_binder()
            elif choice == '3':
                self.view_current_placements()
            elif choice == '4':
                print("Exiting Pokemon Card Binder Manager.")
                break
            else:
                print("Invalid choice. Please try again.")

# Class: Overall Scoring System
class OverallScore:
    def __init__(self):
        self.scores = {
            "GuessNumberGame": 0,
            "RockPaperScissors": 0,
            "TriviaPursuitQuiz": 0
        }

    def update_score(self, game_name, score):
        self.scores[game_name] += score

    def display_scores(self):
        print("\nCurrent Scores:")
        for game, score in self.scores.items():
            print(f"{game}: {score}")

# Class: Game Suite Controller
class GameSuite:
    def __init__(self):
        self.scorer = OverallScore()

    def start(self):
        while True:
            print("\nSelect a function (1-5):")
            print("1. Guess Number Game")
            print("2. Rock Paper Scissors Game")
            print("3. Trivia Pursuit Game")
            print("4. Pokemon Card Binder Manager")
            print("5. Check Current Overall Score")
            print("0. Exit Program")
            try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    game = GuessNumberGame()
                    score = game.play()
                    self.scorer.update_score("GuessNumberGame", 100 - score)  # Invert: fewer guesses = higher score
                elif choice == 2:
                    game = RockPaperScissors()
                    result = game.play()
                    self.scorer.update_score("RockPaperScissors", result)
                elif choice == 3:
                    game = TriviaPursuitQuiz()
                    score = game.play()
                    self.scorer.update_score("TriviaPursuitQuiz", score)
                elif choice == 4:
                    binder = PokemonCardBinder()
                    binder.manage()
                elif choice == 5:
                    self.scorer.display_scores()
                elif choice == 0:
                    print("Exiting program. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

# Entry point
if __name__ == "__main__":
    game_suite = GameSuite()
    game_suite.start()

import random
import TsheringChoden_02240274_A2_PB as pb

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
                ("What is the center of the atom called?", ["Proton", "Neutron", "Nucleus", "Electron"], "Nucleus"),
                ("What do we call material that do not conduct electricity?", ["Conductors", "Insulators", "Reactants", "Transmitters"], "Insulators")
            ],
            "Geography": [
                ("What is the largest continent on Earth?", ["Africa", "Europe", "Asia", "North America"], "Asia"),
                ("Which country is shaped like a boot?", ["Greece", "Italy", "Brazil", "India"], "Italy")
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
Pokemon_card = pb.PokemonCardBinder()
class PokemonCardBinder:
    def __init__(self, overall_score):
        self.overall_score = overall_score
        self.cards = Pokemon_card
        self.session_active = True  # Initialize session_active

    def add_card(self, pokedex_number):
        # Assuming Pokemon_card has an `add_card` method
        try:
            self.cards.add_card(pokedex_number)
            print(f"Pokemon card with Pokedex number {pokedex_number} added successfully.")
        except AttributeError:
            print("Error: Unable to add card. Ensure the PokemonCardBinder is properly initialized.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    
    def reset_binder(self):
        # Assuming Pokemon_card has a `reset_binder` method
        try:
            self.cards.reset_binder()
            print("Binder has been reset successfully.")
        except AttributeError:
            print("Error: Unable to reset binder. Ensure the PokemonCardBinder is properly initialized.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def display_menu(self):
        print("\nMain Menu:")
        print("1. Add Pokemon card")
        print("2. Reset binder")
        print("3. View current placements")
        print("4. Exit")

    def view_placements(self):
        # Assuming Pokemon_card has a `view_placements` method
        try:
            placements = self.cards.view_placements()
            print("Current Placements:")
            for placement in placements:
                print(placement)
        except AttributeError:
            print("Error: Unable to view placements. Ensure the PokemonCardBinder is properly initialized.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def exit_manager(self):
        print("Exiting Pokemon Card Binder Manager.")
        self.session_active = False

    def run(self):
        print("Welcome to Pokemon Card Binder Manager!")
        while self.session_active:
            self.display_menu()
            try:
                choice = int(input("Select option: "))
                if choice == 1:
                    try:
                        pokedex_number = int(input("Enter Pokedex number: "))
                        self.add_card(pokedex_number)
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
                elif choice == 2:
                    self.reset_binder()
                elif choice == 3:
                    self.view_placements()
                elif choice == 4:
                    self.exit_manager()
                else:
                    print("Invalid option. Please choose between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number.")


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
                    binder = PokemonCardBinder(self.scorer)
                    binder.run()
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

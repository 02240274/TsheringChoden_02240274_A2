class PokemonCard:
    """Represents a single Pokemon card entry in the binder."""
    def __init__(self, pokedex_number, page, row, col):
        self.pokedex_number = pokedex_number
        self.page = page
        self.row = row
        self.col = col

    def __str__(self):
        return f"Pokedex #{self.pokedex_number}: Page {self.page}, Position: Row {self.row}, Column {self.col}"


class PokemonCardBinder:
    def __init__(self):
        self.max_pokedex = 1025
        self.cards_per_page = 64  # 8x8 grid
        self.grid_size = 8
        self.cards = {}  # pokedex_number: PokemonCard
        self.session_active = True

    def _recalculate_positions(self):
        """Recalculate positions for all cards to maintain order after addition."""
        sorted_numbers = sorted(self.cards.keys())
        new_cards = {}
        for idx, number in enumerate(sorted_numbers):
            page = idx // self.cards_per_page + 1
            pos = idx % self.cards_per_page
            row = pos // self.grid_size + 1
            col = pos % self.grid_size + 1
            new_cards[number] = PokemonCard(number, page, row, col)
        self.cards = new_cards

    def add_card(self, pokedex_number):
        if not (1 <= pokedex_number <= self.max_pokedex):
            print("Error: Invalid Pokedex number. Must be between 1 and 1025.")
            return

        if pokedex_number in self.cards:
            card = self.cards[pokedex_number]
            print(f"Page: {card.page}")
            print(f"Position: Row {card.row}, Column {card.col}")
            print(f"Status: Pokedex #{pokedex_number} already exists in binder.")
        else:
            self.cards[pokedex_number] = None  # Placeholder
            self._recalculate_positions()
            card = self.cards[pokedex_number]
            print(f"Page: {card.page}")
            print(f"Position: Row {card.row}, Column {card.col}")
            print(f"Status: Added Pokedex #{pokedex_number} to binder.")

    def reset_binder(self):
        print("WARNING: This will delete ALL Pokemon cards from the binder. This action cannot be undone.")
        confirmation = input("Type CONFIRM to reset or EXIT to return to the Main Menu: ").strip().upper()
        if confirmation == "CONFIRM":
            self.cards.clear()
            print("The binder reset was successful! All cards have been removed.")
        elif confirmation == "EXIT":
            print("Binder reset cancelled. Returning to Main Menu.")
        else:
            print("Invalid input. Returning to Main Menu.")

    def view_placements(self):
        if not self.cards:
            print("The binder is empty.")
        else:
            print("Current Binder Contents:")
            for number in sorted(self.cards):
                print(self.cards[number])
        total = len(self.cards)
        print(f"Total cards in binder: {total}")
        percentage = (total / self.max_pokedex) * 100
        print(f"Completion: {percentage:.1f}%")
        if total == self.max_pokedex:
            print("You have caught them all!!")

    def exit_manager(self):
        print("Thank you for using Pokemon Card Binder Manager!")
        self.session_active = False

    def display_menu(self):
        print("\nMain Menu:")
        print("1. Add Pokemon card")
        print("2. Reset binder")
        print("3. View current placements")
        print("4. Exit")

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


if __name__ == "__main__":
    binder = PokemonCardBinder()
    binder.run()

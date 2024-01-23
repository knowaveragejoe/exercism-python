class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")

    def valid(self):
        if not all(num.isnumeric() for num in self.card_num):
            return False

        if len(self.card_num) <= 1:
            return False

        # Local copy so we can call multiple times
        card_num = [int(num) for num in [*self.card_num]]

        odds = card_num[-1::-2]
        evens = card_num[-2::-2]

        checksum = sum(odds)
        for digit in evens:
            product = digit * 2
            if product > 9:
                product -= 9
            checksum += product

        return checksum % 10 == 0

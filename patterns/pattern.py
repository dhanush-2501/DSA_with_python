class Pattern:
    """A class for generating various patterns."""

    def square(self, size: int) -> None:
        """
        Generate a square pattern of '*' characters.

        Args:
            size (int): The size (number of rows and columns) of the square.

        Returns:
            None
        """
        row = '*' * size
        for _ in range(size):
            print(row)

    def lower_triangle(self, size: int) -> None:
        """
        Generate a lower triangle pattern of '*' characters.

        Args:
            size (int): The height (number of rows) of the triangle.

        Returns:
            None
        """
        for i in range(size + 1):
            print('*' * i)

    def upper_triangle(self, size: int) -> None:
        """
        Generate an upper triangle pattern of '*' characters.

        Args:
            size (int): The height (number of rows) of the triangle.

        Returns:
            None
        """
        for i in range(size, 0, -1):
            print('*' * i)

    def upside_triangle(self, size: int) -> None:
        """
        Generate an upside-down triangle pattern of '*' characters.

        Args:
            size (int): The height (number of rows) of the triangle.

        Returns:
            None
        """
        for i in range(1, size + 1):
            space = " " * (size - i)
            star = "*" * (2 * i - 1)
            print(space + star)

    def downSide_triangle(self, size:int) -> None:
        """
        Generate an down side triangle pattern of '*' characters.

        Args:
            size (int): The height (number of rows) of the triangle.

        Returns:
            None
        """
        for i in range(size, 0, -1):
            space = " " * (size - i)
            star = "*" * (2 * i - 1)
            print(space + star)

    def diamond(self, size:int) -> None:
        """
        Generate a sequence of diamond pattern of '*' characters.

        Args:
            size (int): The height (number of rows) of the triangle.

        Returns:
            None
        """
        self.upside_triangle(size)
        self.downSide_triangle(size)

    def arrow(self, size:int) -> None:
        """
        Generate a sequence of arrow pattern of '*' characters.

        Args:
            size (int): The height (number of rows) of the triangle.

        Returns:
            None
        """
        self.lower_triangle(size)
        self.upper_triangle(size - 1)

    def lower_triangle_sequential_numeric(self, size: int) -> None:
        """
        Generate a lower triangle pattern of sequential numeric values.

        Args:
            size (int): The height (number of rows) of the triangle.

        Returns:
            None
        """
        for i in range(1, size + 1):
            for j in range(1, i + 1):
                print(j, end='')
            print()

    def upper_triangle_sequential_numeric(self, size: int) -> None:
        """
        Generate an upper triangle pattern of sequential numeric values.

        Args:
            size (int): The height (number of rows) of the triangle.

        Returns:
            None
        """
        for i in range(size, 0, -1):
            for j in range(1, i + 1):
                print(j, end='')
            print()

    def lower_triangle_continuous_numeric(self, size: int) -> None:
        """
        Generate a lower triangle pattern of continuous numeric values.

        Args:
            size (int): The height (number of rows) of the triangle.

        Returns:
            None
        """
        for i in range(1, size + 1):
            for j in range(1, i + 1):
                print(i, end='')
            print()
    
    def alternate_bin_lower_triangle(self, size: int) -> None:
        """
        Generate a lower triangle pattern of alternate binary values.

        Args:
            size (int): The height (number of rows) of the triangle.

        Returns:
            None
        """
        current = 1
        for i in range(1, size + 1):
            for j in range(1, i + 1):
                print(current, end='')
                current = 1 - current
            print()

    def mirror_numeric_triangle(self, size: int) -> None:
        """
        Generate a mirror triangle pattern of numeric values with aligned endings.

        Args:
            size (int): The height (number of rows) of the triangle.

        Returns:
            None
        """
        max_width = len(str(size))  # Calculate the maximum width of a number in the triangle

        for i in range(1, size + 1):
            # Numbers increasing
            for j in range(1, i + 1):
                print(f"{j:{max_width}}", end='')

            # Calculate space to align endings
            space = 2 * (size - i)
            print("*" * (max_width * space), end='')

            # Numbers decreasing
            for j in range(i, 0, -1):
                print(f"{j:{max_width}}", end='')

            print()  # Move to the next line

    def continous_numeric_lower_triangle(self, size: int) -> None:
        """
        Generate a lower triangle pattern of continous numeric values.

        Args:
            size (int): The height (number of rows) of the triangle.

        Returns:
            None
        """
        current = 1
        for i in range(1, size + 1):
            for j in range(1, i + 1):
                print(current, " ", end='')
                current += 1
            print()

    def alphabet_lower_triangle(self, size):
        """
        Generate a lower triangle pattern of alphabet values.

        Args:
            size (int): The height (number of rows) of the triangle.

        Returns:
            None
        """
        if size < 1:
            return

        current_char = 'A'

        for i in range(1, size + 1):
            for j in range(1, i + 1):
                print(current_char, end=' ')
                current_char = chr(ord(current_char) + 1)
            print()

            

# Example usage:
if __name__ == "__main__":
    pattern = Pattern()
    pattern.square(5)
    pattern.lower_triangle(5)
    pattern.upper_triangle(5)
    pattern.upside_triangle(5)
    pattern.downSide_triangle(5)
    pattern.lower_triangle_sequential_numeric(5)
    pattern.upper_triangle_sequential_numeric(5)
    pattern.lower_triangle_continuous_numeric(5)
    pattern.diamond(5)
    pattern.arrow(5)
    pattern.alternate_bin_lower_triangle(5)
    pattern.mirror_numeric_triangle(10)
    pattern.continous_numeric_lower_triangle(5)


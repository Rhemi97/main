#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int height;

    // Prompt user for height between 1 and 8
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);

    // Loop through each row
    for (int i = 1; i <= height; i++)
    {
        // Print spaces (right-align pyramid)
        for (int j = 0; j < height - i; j++)
        {
            printf(" ");
        }

        // Print hashes
        for (int j = 0; j < i; j++)
        {
            printf("#");
        }

        // Move to next line
        printf("\n");
    }
}

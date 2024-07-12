from zoom import ft_zoom, display_and_save_image
import numpy as np


def transpose(matrix: np.ndarray) -> np.ndarray:
    """
        Transpose the given array
    """
    try:
        rows, cols = len(matrix), len(matrix[0])

        matrixT = []
        for i in range(cols):
            row = []
            for j in range(rows):
                row.append(matrix[j][i])
            matrixT.append(row)

        transposed = np.array(matrixT)

        return transposed

    except Exception as e:
        print(f"Error transposing image: {e}")


def rotate90acw(matrix: np.ndarray) -> np.ndarray:
    """
        Rotate 270 degrees
    """
    try:
        rows = len(matrix)
        cols = len(matrix[0])

        matrixT = []
        for i in range(cols):
            row = []
            for j in range(rows):
                row.append(matrix[j][cols - 1 - i])
            matrixT.append(row)

        rotated = np.array(matrixT)
        return rotated

    except Exception as e:  
        print(f"Error rotating 270 image: {e}")


def ft_rotate():
    try:
        left = 462
        upper = 100
        right = 862
        lower = 500
        mat = ft_zoom("./animal.jpeg", left, upper, right, lower)
        rotated_mat = rotate90acw(mat)
        display_and_save_image(rotated_mat, "croped and rotated image")

    except Exception as e:
        print(f"Error rotating image: {e}")


if __name__ == "__main__":
    ft_rotate()
    
    """ mat = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
        ]
    print(mat)
    mat2 = rotate90acw(mat)
    print(mat2) """

from load_image import ft_load


def ft_zoom(path: str, height: int, width: int) -> None:
    """
        Zoom image by factor
    """
    img = ft_load(path)

    try:
        

        #print(f"The shape of zoomed image is: {}")

    except Exception as e:
        print(f"Error zooming image: {e}")
        
        
if __name__ == "__main__":
    ft_zoom("./animal.jpeg", 2)

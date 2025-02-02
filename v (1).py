import time

def print_hearts():
    hearts = ["❤️", "💛", "💙", "💜", "💖", "💗", "💘", "💝"]
    message = "I love you Manisha"
    
    for i in range(20):  # Number of iterations for the animation
        for heart in hearts:
            print(f"\r{heart} {message} {heart}", end="")
            time.sleep(0.2)  # Adjust the speed of the animation

if __name__ == "__main__":
    print_hearts()
from rich import print
from PIL import Image
import os, random
import shutil

# Image Finder Program
# Author: Liam Gold
# Description: Displays random images based on user input,
# allows users to save images to history, delete them, and clear history

# Default folder paths
image_folder = "images/cat-images"
history_folder = "history"

# Ensure the history folder exists before saving files 
os.makedirs(history_folder, exist_ok=True)

def generate_image():
    #displays a random image from the chosen noun folder
    #saves the image to the history folder if wanted

    #inform user that getting an image may take a moment
    print("[bold blue]Finding an image takes a couple of seconds")

    #ask user to choose a noun category of images (so far only cat/dog)
    noun = input("Enter noun (cat/dog): ")

    #build path to selected noun's image folder
    folder_path = "images/" + noun

    #check if the folder exists
    if not os.path.exists(folder_path):
        print("[bold red]Folder not found. Please enter 'cat' or 'dog'. ")
        return
    #get all images in the desired folder
    all_files = os.listdir(folder_path)

    #get all images in the folder, currently only accepting png
    image_files = [f for f in all_files if f.endswith(".png")]

    #randomly pick one image from the image folder and show its name
    selected_image = random.choice(image_files)
    print(f"[bold green] Selected Image: {selected_image}")  

    #construct full path to the image
    src_path = os.path.join(folder_path, selected_image)

    #ask if the user would like to view the image
    open_image = input("Would you like to view the image? (Yes/No)\n")
    if open_image.lower() == "yes":
        Image.open(src_path).show()     

    #ask if the user would like to save the image to their history folder
    to_history = input("Would you like to save image to history folder? (Yes/No):\n")
    if to_history == "Yes":
        shutil.copy(src_path, history_folder)
    elif to_history == "No":
        print("Press enter to return to menu...\n")

def history():
    #displays saved images in the history folder and allows for deletion
    print("[bold blue]Welcome to the history page. Here you can delete and view saved images.")
    
    folder_path = "history/"

    #get list of saved images in history folder
    all_files = os.listdir(folder_path)

    image_files = [f for f in all_files if f.endswith(".png")]

    #if the history folder is empty, handle it
    images = (image_files)
    if len(images) == 0:
        print("[yellow bold]No images found... ")
        input("Press enter to return to menu...\n")
    else: 
        print("Saved images:", images)

    #allow the user to delete one or more images
    delete_option = input("Would you like to delete an image? (Yes/No): ")

    while delete_option.lower() == "yes":
        print("[bold red]Warning: Deleting an image will permanently remove it from your history folder.\n")
        delete_image = input("Enter the image you would like to delete: ")
        #check if the entered image name exists in history
        if delete_image in os.listdir(folder_path):
            os.remove(os.path.join(folder_path, delete_image))
            print(f"{delete_image} has been deleted.")
        else:
            print("Image not found in history.")
        #ask if they want to delete another iamge
        delete_option = input("Would you like to delete another image? (Yes/No): ")

def settings():
    #allows users to clear all images in their history folder 
    folder_path = "history/"
    print("[bold blue]Welcome to the settings page. Here you can fully clear your image history")

    clear_history = input("Would you like to clear your history? (Yes/No)")
    while clear_history.lower() == "yes":
        print("[bold red]Warning: Clearing your history permanently removes all images in your history folder.\n")

        #get list of all files in the history folder 
        files = os.listdir(folder_path)

        #if the folder is empty, notify the user
        if not files:
            print("History folder is already empty...")
        else:
            #delete all files in history folder
            for file in files:
                os.remove(os.path.join(folder_path, file))
            print("All images have been removed from history")
        clear_history = input("Press enter to return to menu\n")
while True:
    #text-based interface
    print(r"[bold red] __  _  _   __    ___  ____    ____  __  __ _  ____  ____  ____  ")
    print(r"[bold red](  )( \/ ) / _\  / __)(  __)  (  __)(  )(  ( \(    \(  __)(  _ \ ")
    print(r"[bold red] )( / \/ \/    \( (_ \ ) _)    ) _)  )( /    / ) D ( ) _)  )   / ")
    print(r"[bold red](__)\_)(_/\_/\_/ \___/(____)  (__)  (__)\_)__)(____/(____)(__\_) ")

    print("\n[bold blue]Welcome to the Image Finder App! This app helps users find and view \n" \
    "images based on user input nouns stored in the image folders. It also saves and manages\n"
    "image hisotry, making it easy to track and reuse your favorite images.")

    print("\n Select an option:\n 1. Find Image\n 2. View Image History\n 3. Settings\n 4. Exit Program")

    #get user choice
    choice = input("Select a choice between (1-4)\n")

    #menu
    if choice == "1":
        generate_image()
    elif choice == "2":
        history()
    elif choice == "3":
        settings()
    elif choice == "4":
        print("\n[bold red]Exiting program...\n")
        break
    else:
        print("[bold red]Invalid input... Please choose between 1 and 4")
        input("Press enter to return to menu...")



import os
import pygame

# Song data
songs_by_Genre = {
    'pop': ['Jhanjar - Ravneet', 'Bande O Tere Khaas - Barbie Mann', 'Rao Sahab Retro - Vikram Sarkar', 'Proud To Be Desi - Khan Bhaini'],
    'rock': ['Sadda Haq - Mohit Chauhan', 'Bekhayali - Sachet', 'Nadaan Parindey - A.R. Rahman', 'Gallan Goodiyan - Javed Akhtar'],
    'hip-hop': ['City Slum - Divine', 'Level Up - Ikka', 'Lose Yourself - Eminem', '36 - Raftaar'],
    'jazz': ['Take Five - Dave Brubeck', 'So What - Miles Davis', 'Feeling Good - Nina Simone'],
    'classical': ['Canon in D - Pachelbel', 'Clair de Lune - Debussy', 'Raga Yaman - Ustad Rashid Khan']
}

songs_by_Mood = {
    'happy': ['Rain Over Me - Pitbull', 'Mere Jigar Ka Challa - Harjeet Deewana', 'Paisa On My Mind - KR$NA', 'IICONIC - King'],
    'sad': ['Baarishein - Anuv Jain', 'LOST - Dino James', 'Waasta - Prabh Gill', 'Duniya Makkaar - Karma'],
    'relaxed': ['Agg Banke - Talwiinder', 'Spellbound - Dhanda Nyoliwala', 'Damru Ala - Bila Sonipat Ala', 'Gurjari - MC SQUARE'],
    'energetic': ['Tera Yaar Jamanat Pe Aaya - Raj Mawer', 'Ego Killer - Dhanda Nyoliwala', 'Bonjour - Dhanda Nyoliwala', '7 Seater - vkey']
}

songs_by_Artist = {
    'dhanda nyoliwala': ['Death Row', 'Russian Bandana', 'Ego Killer', 'Block'],
    'addy nagar': ['LETS FIGHT', 'Beat Pe Haley', 'Kaley Sheshe', 'SAKSHAM'],
    'billa sonipat ala': ['Over Confidence', 'Eyes 44', 'Fallin Star', 'Albadi Hood'],
    'mc square': ['2 woofer', 'Tedhe Chaalak', 'Pitbull', 'Mashooka']
}

def play_song(song_name):
    """
    Function to play a song using pygame.
    """
    folder_path = "./songs"  # Replace with your actual folder path
    file_path = os.path.join(folder_path, song_name + ".mp3")
    
    if os.path.exists(file_path):
        print(f"\nNow playing: {song_name}")
        
        # Initialize pygame mixer and play the song
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        
        while pygame.mixer.music.get_busy():
            user_input = input("Type 'stop' to stop the song: ").strip().lower()
            if user_input == 'stop':
                pygame.mixer.music.stop()
                break
    else:
        print(f"Sorry, the file for '{song_name}' was not found in the folder '{folder_path}'.")

def recommend_by_Genre(genre):
    genre = genre.lower()
    if genre in songs_by_Genre:
        print(f"\nBased on your interest in {genre} music, I recommend:")
        for i, song in enumerate(songs_by_Genre[genre], 1):
            print(f"{i}. {song}")
        choice = input("\nEnter the number of the song you'd like to play: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(songs_by_Genre[genre]):
            selected_song = songs_by_Genre[genre][int(choice) - 1].split(" - ")[0]
            play_song(selected_song)
        else:
            print("Invalid choice.")
    else:
        print(f"Sorry, I don't have recommendations for the genre '{genre}'.")

def recommend_by_Mood(mood):
    mood = mood.lower()
    if mood in songs_by_Mood:
        print(f"\nSince you're feeling {mood}, here are some songs for you:")
        for i, song in enumerate(songs_by_Mood[mood], 1):
            print(f"{i}. {song}")
        choice = input("\nEnter the number of the song you'd like to play: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(songs_by_Mood[mood]):
            selected_song = songs_by_Mood[mood][int(choice) - 1].split(" - ")[0]
            play_song(selected_song)
        else:
            print("Invalid choice.")
    else:
        print(f"Sorry, I don't have recommendations for the mood '{mood}'.")

def recommend_by_Artist(artist):
    artist = artist.lower()
    if artist in songs_by_Artist:
        print(f"\nHere are songs by {artist.title()}:")
        for i, song in enumerate(songs_by_Artist[artist], 1):
            print(f"{i}. {song}")
        choice = input("\nEnter the number of the song you'd like to play: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(songs_by_Artist[artist]):
            selected_song = songs_by_Artist[artist][int(choice) - 1]
            play_song(selected_song)
        else:
            print("Invalid choice.")
    else:
        print(f"Sorry, I don't have songs by the artist '{artist}'.")

def chatbot():
    """
    Main chatbot function to recommend songs and play them.
    """
    print("Welcome to the Music Recommendation Bot!")
    print("You can get recommendations by Genre, Mood, or Artist and play songs.")
    print("Type 'exit' at any time to end the conversation.")
    
    while True:
        print("\nHow would you like recommendations? (Genre/Mood/Artist)")
        user_choice = input("Enter 'genre', 'mood', 'artist', or 'exit': ").strip().lower()
        
        if user_choice == 'exit':
            print("Goodbye!")
            break
        elif user_choice == 'genre':
            genre = input("Enter a Genre (e.g., pop, rock, hip-hop, jazz, classical): ").strip()
            recommend_by_Genre(genre)
        elif user_choice == 'mood':
            mood = input("Enter your Mood (e.g., happy, sad, relaxed, energetic): ").strip()
            recommend_by_Mood(mood)
        elif user_choice == 'artist':
            artist = input("Enter an Artist's name (e.g., dhanda nyoliwala , addy nagar , billa sonipat Ala , mc square ): ").strip()
            recommend_by_Artist(artist)
        else:
            print("Invalid choice. Please type 'genre', 'mood', 'artist', or 'exit'.")

if __name__ == "__main__":
    chatbot()
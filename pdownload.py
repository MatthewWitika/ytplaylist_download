import requests
from pytube import Playlist

# Function to download videos from a YouTube playlist URL
def download_playlist_videos(url):
    playlist = Playlist(url)
    print(f"Downloading {len(playlist)} videos from the playlist...")
    for video in playlist.videos:
        try:
            print(f"Downloading {video.title}...")
            video.streams.get_highest_resolution().download(output_path="./downloads")
            print(f"{video.title} downloaded successfully!")
        except Exception as e:
            print(f"Error downloading {video.title}: {e}")

# Example usage
if __name__ == "__main__":
    playlist_url = input("Enter the YouTube playlist URL: ")
    download_playlist_videos(playlist_url)

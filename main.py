from pytube import YouTube
from pytube.cli import on_progress
from tqdm import tqdm

def get_video_streams(url):
    try:
        # Create a YouTube object with the provided URL
        yt = YouTube(url, on_progress_callback=on_progress)

        # Fetch all available video streams
        streams = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()

        # Display available resolutions and their sizes
        stream_list = []
        print("Available streams:")
        for i, stream in enumerate(streams):
            size_in_mb = stream.filesize / (1024 * 1024)
            print(f"{i + 1}. Resolution: {stream.resolution}, Size: {size_in_mb:.2f} MB")
            stream_list.append(stream)
        return stream_list
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def download_youtube_video(stream):
    try:
        # Download the selected video stream with progress bar
        stream.download()
        print("Download completed!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Prompt the user to enter the YouTube URL
    url = input("Please enter the YouTube URL: ")

    # Get available video streams
    streams = get_video_streams(url)
    if streams:
        # Prompt the user to choose a resolution
        choice = int(input("Enter the number of the stream to download: ")) - 1

        if 0 <= choice < len(streams):
            # Download the selected stream
            download_youtube_video(streams[choice])
        else:
            print("Invalid choice.")
    else:
        print("No streams available or an error occurred.")

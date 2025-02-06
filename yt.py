from yt_dlp import YoutubeDL

while True:
    try:
        
        url = input("\nEnter the YouTube URL (or type 'exit' to quit): ")
        
        # Check if the user wants to exit
        if url.lower() == 'exit':
            print("Closing the program, Have a nice day!")
            break

        # Configure yt-dlp options
        ydl_opts = {
            'format': 'best',  # Download the best quality available
            'quiet': True,     # Dont show the long downloading process and components being downloaded
        }

        # Create a YoutubeDL object and as assigns it to variable ydl
        with YoutubeDL(ydl_opts) as ydl:
            
            info_dict = ydl.extract_info(url, download=False)
            # Grabs the video info without having to download it
            
            # Print video details
            print("\nTitle:", info_dict.get('title', 'Unknown'))
            print("Views:", info_dict.get('view_count', 'Unknown'))
            #Use if statement for duration to get a more accurate number
            duration_seconds = info_dict.get('duration', 'Unknown')

            if duration_seconds != 'Unknown':  # If no error/time is known then do below
                hours, remainder = divmod(duration_seconds, 3600)  # Convert seconds to hours and remainder
                minutes, seconds = divmod(remainder, 60)  # Convert remainder to minutes and seconds
                print(f"Duration: {hours}:{minutes:02}:{seconds:02}")  # Format as HH:MM:SS
            else:
                print("Duration: Unknown")


            # Download the video
            print("\nDownloading...")
            ydl.download([url])
            print("Download complete!")

    except Exception as e:
        print("An error occurred:", str(e))
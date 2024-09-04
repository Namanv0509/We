import streamlit as st
import requests

def youtube_audio_player(playlist_id, api_key):
    # Generate the embed URL for the YouTube playlist
    embed_url = f"https://www.youtube.com/embed/videoseries?list={playlist_id}&autoplay=1&loop=1&controls=0&modestbranding=1"
    
    # Embed the YouTube player with CSS to hide the video and style the controls
    st.markdown(f"""
    <style>
    .video-container {{
        position: relative;
        padding-bottom: 20px;
        height: 0;
        overflow: hidden;
        max-width: 300px;
        background: #000;
        color: white;
    }}
    .video-container iframe {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        border: 0;
        visibility: hidden; 
    }}
    .video-container .video-info {{
        margin-top: 10px;
    }}
    </style>

    <div class="video-container">
        <iframe id="youtube-player" src="{embed_url}" allow="autoplay; encrypted-media" allowfullscreen></iframe>
        <div class="video-info">
            <h4 id="video-title">Loading...</h4>
        </div>
    </div>

    <script>
    // Function to fetch the playlist data and get the title of the currently playing video
    function updateVideoTitle() {{
        fetch('https://www.googleapis.com/youtube/v3/playlists?part=snippet&id={playlist_id}&key={api_key}')
        .then(response => response.json())
        .then(data => {{
            const playlistTitle = data.items[0].snippet.title;
            document.getElementById('video-title').textContent = playlistTitle;
        }})
        .catch(error => console.error('Error fetching playlist title:', error));
    }}

    
    updateVideoTitle();

    
    function controlVideo(action) {{
        const player = document.getElementById('youtube-player');
        if (action === 'next') {{
            player.src += '&index=1';  // Move to next video
        }} else if (action === 'prev') {{
            player.src += '&index=-1'; // Move to previous video
        }} else if (action === 'pause') {{
            player.src = player.src.replace('&autoplay=1', ''); // Pause video
        }}
        updateVideoTitle();
    }}

    
    document.addEventListener('keydown', function(event) {{
        if (event.key === 'L') {{
            controlVideo('next');
        }} else if (event.key === 'K') {{
            controlVideo('prev');
        }} else if (event.key === 'P') {{
            controlVideo('pause');
        }}
    }});
    </script>
    """, unsafe_allow_html=True)

playlist_id = "PLPsCmCn1OJNF5Vrot2-FySMLkeCN_Gjan"  # Replace with your YouTube playlist ID
api_key = "AIzaSyDbf2gi8zRU5SHOjfwYb6pbko2gi6fsq5U"  # Replace with your YouTube Data API key

# --- Main Streamlit App Setup ---
def main():
    about_page = st.Page(
        page="views/about_me.py",
        title="About Me",
        icon=":material/favorite:",
        default=True,
    )

    project_1_page = st.Page(
        page="views/meow_dashboard.py",
        title="Meow Dashboard",
        icon=":material/face_5:",
    )

    project_2_page = st.Page(
        page="views/chatbot.py",
        title="Chat Bot",
        icon=":material/smart_toy:",
    )

    project_3_page = st.Page(
        page="views/poems.py",
        title="Poem",
        icon=":material/stylus:",
    )

    project_4_page = st.Page(
        page="views/meow_menu.py",
        title="Meow Menu🐱👩‍🍳",
        icon=":material/menu_book:",
    )

    # -- Navigation setup [without sections] --
    pg = st.navigation(
        {
            "Info": [about_page],
            "Meowing": [project_1_page, project_2_page, project_3_page, project_4_page],
        }
    )

    # -- Shared on all pages --
    st.logo("assets/Totoro png.png")
    st.sidebar.text("Catio")

    # -- Embed the YouTube Player on all pages --
    youtube_audio_player(playlist_id, api_key)

    # -- Run navigation --
    pg.run()

if __name__ == "__main__":
    main()

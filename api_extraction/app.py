from googleapiclient.discovery import build
import csv
API_KEY = "AIzaSyC13r0vEHAFncRPHNdvHWQ4abnBf-3T5Ds"
youtube = build('youtube','v3',developerKey = API_KEY)

search_response = youtube.search().list(
    q="Physics Wallah",
    type="channel",
    part="id,snippet",
    maxResults=1
).execute()

channel_id = search_response['items'][0]['id']['channelId']
print("Channel ID:", channel_id)

channel_response = youtube.channels().list(
    part="contentDetails",
    id=channel_id
).execute()

playlist_id = channel_response['items'][0]['contentDetails']['relatedPlaylists']['uploads']
print("Uploads Playlist ID:", playlist_id)

video_ids = []
next_page_token = None

while True:
    playlist_response = youtube.playlistItems().list(
        part = "contentDetails",
        playlistId = playlist_id,
        maxResults = 50,
        pageToken = next_page_token
    ).execute()

    for item in playlist_response['items']:
        video_ids.append(item['contentDetails']['videoId'])
    next_page_token = playlist_response.get('nextPageToken')
    if not next_page_token:
        break
video_data = []
for i in range(0,len(video_ids),50):
    batch_ids = video_ids[i:i+50]
    video_response = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        id=','.join(batch_ids)
    ).execute()
    for video in video_response['items']:
        snippet = video['snippet']
        stats = video['statistics']
        details = video['contentDetails']
        video_data.append({
            "video_id": video['id'],
            "title": snippet['title'],
            "description": snippet.get('description', ''),
            "publishedAt": snippet['publishedAt'],
            "tags": ",".join(snippet.get('tags', [])),
            "categoryId": snippet.get('categoryId', ''),
            "duration": details.get('duration', ''),
            "viewCount": stats.get('viewCount', 0),
            "likeCount": stats.get('likeCount', 0),
            "commentCount": stats.get('commentCount', 0)
        })

print(f"Total videos with details: {len(video_data)}")
csv_file = "physics_wallah_videos.csv"

with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=video_data[0].keys())
    writer.writeheader()
    writer.writerows(video_data)

print(f"Video details exported to {csv_file}")

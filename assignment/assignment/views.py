from django.http import HttpResponse
from models import *
from apiclient.discovery import build 
import threading
from datetime import datetime,timedelta
import json

DEVELOPER_KEY = "AIzaSyAK5kEBFnEE-UTrYWXu-rBahKza4uUddig"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
youtube_object = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey = DEVELOPER_KEY) 
published_after="2020-01-01T00:00:00Z"
published_before=datetime.today().strftime('%Y-%m-%dT%H:%M:%SZ')
count = 1
# creating Youtube Resource Object 
def youtube_search_keyword(query, max_results): 

    try:
        # calling the search.list method to 
        # retrieve youtube search results 

        global published_after
        global published_before
        global count
        print published_before
        search_keyword = youtube_object.search().list(q = query, type ='video', part = "id, snippet", maxResults = max_results,order="date",publishedAfter=published_after,publishedBefore=published_before).execute()

        # extracting the results from search response 
        results = search_keyword.get("items", [])

        # empty list to store video 
        videos = []

        # extracting required info from each result object 
        for result in results:
            # video result object 
            if result['id']['kind'] == "youtube#video": 
                details = {}
                details['title'] = result["snippet"]["title"].strip()
                details['id'] = result["id"]["videoId"].strip()
                details['desc'] = result['snippet']['description'].strip() 
                details['url'] = result['snippet']['thumbnails']['default']['url'].strip()
                details['published_at'] = result['snippet']['publishedAt']
                YoutubeVideos(video_id=details['id'], title=details['title'], description=details['desc'], published_at=details['published_at'], default_url=details['url']).save()
                videos.append(details)

        if(len(videos) > 0):
            published_before=videos[-1]['published_at']
        else:
           count = 0
        count -= 1
        print count
        if(count > 0):
            t = threading.Timer(10.0, youtube_search_keyword(query, max_results = 10))
            t.start()
            t.cancel()
    except Exception as error:
        print "Exception Occured during Insertion of videos: " + str(error)


def insert_videos(request, search_keyword):
    youtube_search_keyword(search_keyword, max_results = 10)
    return HttpResponse("SUCCESSFULLY INSERTED!")

def get_videos(request):
    video_data = []
    try:
        youtubevideos_obj = YoutubeVideos.objects.all().order_by('published_at')
        if youtubevideos_obj is not None:
            for data in youtubevideos_obj:
                output = {}
                output['VideoId'] = data.video_id
                output['Title'] = data.title
                output['Description'] = data.description
                output['Thumbnails Default Url'] = data.default_url
                output['Published At'] = data.published_at
                video_data.append(output)
    except Exception as error:
        print "Exception Occured during getting videos content: " + str(error)
    return HttpResponse(video_data)

def search_videos(request, title, description):
    video_data = {}
    output_list = []
    video_data["Title"] = str(title)
    video_data["Description"] = str(description)
    video_data['Content'] = []
    try:
        youtubevideos_obj = YoutubeVideos.objects.filter(title=title,description=description).order_by('published_at')
        if youtubevideos_obj is not None:
            for data in youtubevideos_obj:
                output = {}
                output['VideoId'] = str(data.video_id)
                output['Title'] = str(data.title)
                output['Description'] = str(data.description)
                output['Thumbnails Default Url'] = str(data.default_url)
                output['Published At'] = data.published_at
                video_data['Content'].append(output)
    except Exception as error:
        print "Error Occured during Searching of videos: " + str(error)

    output_list.append(video_data)
    return HttpResponse(output_list)

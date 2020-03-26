from googleapiclient.discovery import build

class YoutubeAPI:

    def __init__(self,api_key):
        print("> YouTube API initialized")
        self.api_key = api_key
        self.youtube = build('youtube', 'v3', developerKey=api_key)


    # Creates a dataset of approximately 20000 videos
    def createDataset(self):
        # No I did not create a list/dir with YouTube channels. Deal with it!
        self.getChannelVideos('UCX6OQ3DkcsbYNE6H8uQQuVA', 'Mr Beast')  # Mr Beast
        self.getChannelVideos('UC-lHJZR3Gqxm24_Vd_AJ5Yw', 'PewDiePie')  # PewDiePie
        self.getChannelVideos('UCmh5gdwCx6lN7gEC20leNVA', 'David Dobrik')  # David Dobrik
        self.getChannelVideos('UCY30JRSgfhYXA6i6xX1erWg', 'Smosh')  # Smosh
        self.getChannelVideos('UC4PooiX37Pld1T8J5SYT-SQ', 'GMM')  # GMM
        self.getChannelVideos('UC295-Dw_tDNtZXFeAPAW6Aw', '5 Minute Crafts')  # 5 Minute Crafts
        self.getChannelVideos('UCtinbF-Q-fVthA0qrFQTgXQ', 'Casey Neistat')  # Casey Neistat
        self.getChannelVideos('UCYJPby9DRCteedh5tfxVbrw', 'Smosh Pit')  # Smosh Pit
        self.getChannelVideos('UCV9_KinVpV-snHe3C3n1hvA', 'Shane')  # Shane
        self.getChannelVideos('UCpIafFPGutTAKOBHMtGen7g', 'Gus')  # Gus
        self.getChannelVideos('UCwCI06WrrkGr1VyhkQMFBlw', 'Elle Mils')  # Elle Mils
        self.getChannelVideos('UC3tMH8u6yG3mSxi-qpfmpkA', 'Tomaska 2')  # Tomska 2
        self.getChannelVideos('UCGwu0nbY2wSkW8N-cghnLpA', 'Jaiden Animations')  # Jaiden Animations
        self.getChannelVideos('UCn1XB-jvmd9fXMzhiA6IR0w', 'Domics')  # Domics
        self.getChannelVideos('UCoLUji8TYrgDy74_iiazvYA', 'Jarvis Johnson')  # Jarvis Johnson
        self.getChannelVideos('UCucot-Zp428OwkyRm2I7v2Q', 'James Chaarles')  # James Charles
        self.getChannelVideos('UCY1kMZp36IQSyNx_9h4mpCg', 'Mark Ropper')  # Mark Roper
        self.getChannelVideos('UC3iNdSV_RQU7DHTGpqEW96w', 'Andrei Terbea')  # Andrei Terbea
        self.getChannelVideos('UC3KEoMzNz8eYnwBC34RaKCQ', 'Simon Giertz')  # Simon Giertz
        self.getChannelVideos('UCQL5ABUvwY7YoW5lgMyAS_w', 'Wheezy Waiter')  # Wheezy Waiter
        self.getChannelVideos('UCPJHQ5_DLtxZ1gzBvZE99_g', 'Anthony Padilla')  # Anthony Padilla
        self.getChannelVideos('UCJ24N4O0bP7LGLBDvye7oCA', 'Matt D Avella')
        self.getChannelVideos('UCrdWRLq10OHuy7HmSckV3Vg', 'Nathanel Drew')
        self.getChannelVideos('UC6MXE0Px3m1aI4vI0pLWzQg', 'Goal Guys')
        self.getChannelVideos('UC6nSFpj9HTCZ5t-N3Rm3-HA', 'Vsauce')
        self.getChannelVideos('UCPDXXXJj9nax0fr0Wfc048g', 'College Humor')
        self.getChannelVideos('UCt_t6FwNsqr3WWoL6dFqG9w', 'Brain Craft')
        self.getChannelVideos('UCSAUGyc_xA8uYzaIVG6MESQ', 'nigahiga')
        self.getChannelVideos('UCwmFOfFuvRPI112vR5DNnrA', 'Vsauce 3')
        self.getChannelVideos('UCo8bcnLyZH8tBIH9V1mLgqQ', 'The Odd1sout')
        self.getChannelVideos('UCG-KntY7aVnIGXYEBQvmBAQ', 'Thomas Frank')
        self.getChannelVideos('UCo_IB5145EVNcf8hw1Kku7w', 'The Game Theorists')
        self.getChannelVideos('UCZfPrUL62TN74Mmrn-O_pZQ', 'Dan Mace')
        self.getChannelVideos('UCqHZdrDcZhhRO11m67Tgz4A', 'Swoop')
        self.getChannelVideos('UCaN8ossBe8E195tJTl_6ROA', 'Brad 2 (Aloona)')
        self.getChannelVideos('UCsXVk37bltHxD1rDPwtNM8Q', 'Kurzgeagt')
        self.getChannelVideos('UCHnyfMqiRRG1u-2MsSQLbXA', 'Veritasium')
        self.getChannelVideos('UCN5xN8gIljvWYnsj06V8WbQ', 'Pyrocynical')
        self.getChannelVideos('UCqmugCqELzhIMNYnsjScXXw', 'Vsauce2')
        self.getChannelVideos('UC7_YxT-KID8kRbqZo7MyscQ', 'Markipiler')
        self.getChannelVideos('UCYzPXprvl5Y-Sf0g4vX-m6g', 'Jackcepticeye')
        self.getChannelVideos('UCC552Sd-3nyi_tk2BudLUzA', 'ASAPScience')
        self.getChannelVideos('UCV6KDgJskWaEckne5aPA0aQ', 'Graham Stephan')
        self.getChannelVideos('UCtUId5WFnN82GdDy7DgaQ7w', 'Better Ideas')
        self.getChannelVideos('UCO79NsDE5FpMowUH1YcBFcA', 'Johnathan Pie')
        self.getChannelVideos('UC3DkFux8Iv-aYnTRWzwaiBA', 'Peter McKinnon')
        self.getChannelVideos('UCaXEr4t_QBZBk3qlIlc2HRg', 'Jenelle Eliana')
        self.getChannelVideos('UCxsQFG_8Dbt1sZhLReL2mUw', 'Nerd City')
        self.getChannelVideos('UC_24l4maHg3zqqVPOknCKfw', 'Brave Wilderness')
        self.getChannelVideos('UCFQMnBA3CS502aghlcr0_aw', 'Cofeezila')
        self.getChannelVideos('UCbYzlEUtmKsvkzyVm6rPPlQ', 'Garrett')
        self.getChannelVideos('UCpi8TJfiA4lKGkaXs__YdBA', 'The Try guys')
        self.getChannelVideos('UC1x4XiKjnt_aonVhDLDxqmw', 'Jessie Page')
        self.getChannelVideos('UCDVPcEbVLQgLZX0Rt6jo34A', 'Mr Kate')

        # Lowlifes
        self.getChannelVideos('UCBwSufNse8VMBvQM_rCSvgQ', 'Morgz')
        self.getChannelVideos('UCcgVECVN4OKV6DH1jLkqmcA', 'Jake Paul')
        self.getChannelVideos('UCG8rbF3g2AMX70yOd8vqIZg', 'Logan Paul')


    def getChannelVideos(self,channel_id, youtuber):

        f = open("titles.txt", "a", encoding='utf-8')

        res = self.youtube.channels().list(id=channel_id, part='contentDetails').execute()
        playlist_id = res['items'][0]['contentDetails']['relatedPlaylists']['uploads']

        # print("ChannelID: ",channel_id+" Uploads: ",playlist_id)
        videos = []
        next_page = None

        limit = 0
        titleLen = 0
        while 1 and limit < 14:
            limit += 1
            res = self.youtube.playlistItems().list(playlistId=playlist_id, part='snippet', maxResults=50,
                                               pageToken=next_page).execute()
            video_items = res['items']
            for item in video_items:
                # print(item['snippet']['title'])
                f.write(item['snippet']['title'] + '\n')
                videos.append(item['snippet']['title'])
                titleLen += len(item['snippet']['title'])

            if "nextPageToken" not in res:
                break

            next_page = res['nextPageToken']

        print(youtuber, " videos: ", len(videos), ' av title len: ', titleLen / len(videos))
        f.close()
        return videos
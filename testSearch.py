import soundcloud

client=soundcloud.Client(client_id='5DeoP85oSz6LoxhpVvEwf4d9eJHUBRKP')

tracks=client.get("/tracks", genres='techno', bpm={'from':140})
for track in tracks:
     for k, v in track.fields().items():
          print "{}: {}".format(k, v)
import os

paths = ['badminton', 'canoe', 'park', 'parking', 'pedestrians',
         'peopleInShade', 'tramCrossroad_1fps', 'turbulence3', 'wetSnow', 
         'winterStreet', 'zoomInZoomOut']

print("badminton input:", len(os.listdir('badminton/input')))
print("badminton groundtruth:", len(os.listdir('badminton/groundtruth')))

print("canoe input:", len(os.listdir('canoe/input')))
print("canoe groundtruth:", len(os.listdir('canoe/groundtruth')))

print("park input:", len(os.listdir('park/input')))
print("park groundtruth:", len(os.listdir('park/groundtruth')))

print("parking input:", len(os.listdir('parking/input')))
print("parking groundtruth:", len(os.listdir('parking/groundtruth')))

print("pedestrians input:", len(os.listdir('pedestrians/input')))
print("pedestrians groundtruth:", len(os.listdir('pedestrians/groundtruth')))

print("peopleInShade input:", len(os.listdir('peopleInShade/input')))
print("peopleInShade groundtruth:", len(os.listdir('peopleInShade/groundtruth')))

print("tramCrossroad_1fps input:", len(os.listdir('tramCrossroad_1fps/input')))
print("tramCrossroad_1fps groundtruth:", len(os.listdir('tramCrossroad_1fps/groundtruth')))

print("turbulence3 input:", len(os.listdir('turbulence3/input')))
print("turbulence3 groundtruth:", len(os.listdir('turbulence3/groundtruth')))

print("wetSnow input:", len(os.listdir('wetSnow/input')))
print("wetSnow groundtruth:", len(os.listdir('wetSnow/groundtruth')))

print("winterStreet input:", len(os.listdir('winterStreet/input')))
print("winterStreet groundtruth:", len(os.listdir('winterStreet/groundtruth')))

print("zoomInZoomOut input:", len(os.listdir('zoomInZoomOut/input')))
print("zoomInZoomOut groundtruth:", len(os.listdir('zoomInZoomOut/groundtruth')))
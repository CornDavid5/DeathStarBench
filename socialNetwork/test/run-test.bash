#!/bin/bash

for f in TestUniqueIdService.py TestUrlShortenService.py TestUserService.py TestUserMentionService.py TestPostStorage.py TestSocialGraph.py TestTextService.py TestUserTimelineService.py TestWriteHomeTimelineService.py TestReadHomeTimelineService.py testComposePost.py TestComposePostE2E.py
do
    python3 "$f" 2>&1
done
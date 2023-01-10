#!/bin/bash

for f in testCastInfoService.py testUserService.py testMovieIdService.py testPlotService.py testRatingService.py testTextService.py testUniqueIdService.py testReviewStorageService.py testUserReviewService.py testMovieReviewService.py testComposeReviewService.py testComposeReviewServiceE2E.py
do
    python3 "$f" 2>&1
done
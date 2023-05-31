
%% Reading the image sequence
close all 
videoReader = VideoReader('Pattern.mp4');

videoPlayer  = vision.VideoPlayer;
objectFrame = readFrame(videoReader );
imshow(objectFrame)
axis on 
hold on
[x,y] = ginput(5)
%%
objectRegion=  [  431.5100  190.5100  874.9800  718.9800]

objectImage = insertShape(objectFrame,'rectangle',objectRegion,'Color','red');
figure;
imshow(objectImage);
title('Red box shows object region');

%% Kaze feature qui a été remplacé par ginput
points =  detectKAZEFeatures(im2gray(objectFrame),'ROI',objectRegion);
imshow(objectFrame); hold on;
points=points.selectStrongest(500)
plot(points);




%%
loc=[x y]
tracker = vision.PointTracker('MaxBidirectionalError',1);
initialize(tracker,loc,objectFrame);
i=1
trackedPointsPerFrame=[[]]
while hasFrame(videoReader)
      i=i+1;
      frame = readFrame(videoReader);
      [points,validity] = tracker(frame);
      out = insertMarker(frame,points(validity, :),'+');
      step(videoFWriter,out );
      trackedPointsPerFrame=[trackedPointsPerFrame;points(validity, :)];
      videoPlayer(out);
end
release(videoPlayer);
% trackedPointsPerFrame Contains the coordinates of the four points in each
% frame length(trackedPointsPerFrame)/359=4.9861 and not the expected 5
% since some points are not tracked 
trackedPointsPerFrame



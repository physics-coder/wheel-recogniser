<h1> Welcome to the journal! </h1>
<h2> Day 1: 12 December (and the night before 13)</h2>
<p> On this day I created the first version of the wheel and learnt about the HoughCircle function. My code was able to receive video input, detect the wheel and draw only
the contours within it on screen.</p>
<p> Here is how the wheel looked like: </p>
<img width="610" alt="Screenshot 2022-12-17 at 10 11 43" src="https://user-images.githubusercontent.com/81472865/208230380-bf750053-549e-402a-8aed-63dd712a5622.png">
<h2> Day 2: 13 December</h2>
<p> This was a big day for the project, because I revamped the wheel. I made it smaller, and glued a white paper onto it, so the background is more neutral.
The tick (detection rectangle) was cut out of bright red paper and glued on as well, so now it was detected as one four-sided contour, when simplified. 
<p> The reason for the tick being red was so that I could mask the colour out and avoid detecting random contours. This would later allow me to tell
if the wheel was actually detected and it is not a random circle (by checking if it contains a light red rectangle).</p>
<h2> Day 3: 14 December</h2>
<p> On this day I was tuning the masking and realised red was a bad colour to pick, because not only did it interfere with the hands holding the wheel, 
but also required to masks for detection. For this reason in the evening I changed the tick to be light blue. I also figured out how to regulate
sensitivity in "wasd" games and hard coded the values through the dot product. </p>
<p> This is how the final version of the wheel looked like: </p>
<img width="565" alt="Screenshot 2022-12-17 at 10 24 35" src="https://user-images.githubusercontent.com/81472865/208230779-94852d9d-151a-442b-ac82-279cc4de69a5.png">
<h2> Day 4: 15 December</h2>
<p> Basically the whole day was spent tweaking the recognition parameters and sensitivity, so the wheel could work in different lighting conditions </p>
<h2> Day 5: 16 December (and the night onto 17) </h2>
<p> This was the day I created my video interface. I learnt how to mingle together opencv and tkinter, played around with the settings and their order in tkinter.
I also created custom presets for sensitivity levels and changed the angle values from being hard coded with the dot product to relying on the cosinus of the
angle, which meant I could hold the wheel at any distance now. I also created a helpful system, that is used to show the user if the wheel is in camera and upright
to start. Finally, I did some optimizations, such as removing the "try-except" statement, removed unnessecary code lines, added comments. </p>
<p> This is how my final interface looks like! </p>
<img width="901" alt="Screenshot 2022-12-17 at 10 45 59" src="https://user-images.githubusercontent.com/81472865/208231618-2472a5a5-d1ee-43ad-8e87-95f1b0126121.png">

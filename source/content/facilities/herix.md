title: Tutorial for Single crystal HERIX measurements
url: facilities/herix.html
save_as: facilities/herix.html


**GETTING ORIENTATION MATRIX FOR SINGLE CRYSTALS USING GSA-ADA **

**Ver. 1**

**October 2013**

## 1. Introduction:

This manual describes a procedure for finding orientation matrix (UB
matrix) for single crystal.  Data is collected from Perkin Elmer (PE)
flat panel 2D detector.   PE detector control can be opened by clicking
“*_epics**” icon that runs the **epics** as well.  GSA-ADA is
witten in IDL code.

There are three stages for obtaining UB matrix:

-   Collecting data usi_DC units,,
-   Analyzing  data wih GSA-ADA
-   Extracting orientation matrix by RSV utility.

## 1. Collecting data:

-   First open IDL 6.4 version.  GSA-ADA and its utilities works with
    version and not with version 8.0.
-   Sele_DC.prj under **FileRecent
    ProectsC:3_DC.prj**.
-   Compile al files under **ProjectCompileAll Files**twice.
-   And run project under **Project Run**.  This will bring two new
    windows _DC and CCD Image**).
-   _DC winow, by clicking “**EPICS Config**” on the upper right
   corner connect to EPICS configuration for controlling and recording
    motor positions.  
-   It brings another window named **EPICS Configuration**.  If the
    motor names have not been changed, there is nothing to do for the
    fields.  Make sure motor names are correct.  Then click
    **“CONNECT”** bottom on the lower side.
-   Program will be ready when **EPICS Configuration** window closes
    itself and shows **Connected****message in the **EPICS
    Connection**field in the main_DC** window.  This might take
    up to a mi
Program collects data from defined positions of the translational stages
and one can define up to five different samples placed on the stage. 
Depending on how many samples you have, one can enter those positions by
moving XYZ translational stages to specific sample.

Currently Kohzu X (m50), Kohzu Y (m51) and Kohzu Z (m52) set as sample
translational sta
-   Click on **“define”** bottom.  It will read the position of the
    sample X, Y, Z .
-   To collect data from this sample position, check the field says
    **“collect”**.
-   Collection of the data is done by rotating Phi circle. 

 In order to do this, check and write the range of rotation you would
like to do in the fields.  It is given as **start** (at -15 degree),
**total range**(30 degree), **number of steps** (30) and **exp. Time per
deg.** (1 sec).  

This will do phi rotation of -15 to +15 degree in 30 steps with 1 sec
exposure time and it will only take about 30 seconds.

-   Also define name and directory where the files will be saved.  This
    can be done  by selecting directory name in field on the top left
    side called **“NTFS dir”**.  WriteUs_AUG13” and
    “sample name” li_D1.  Define star #” like
    001.*
-   Finally check **‘start Exposure”**to collect data. ***Make sure to
    open station shutter before collecting data.  Currently it is not
    connected to shutters***. Program moves the motor to position.  For
    this starts speed of zero.  Then motor moves ahead of the position
    (like to -15.5).  Then starts recording at -15 degree.  ***NOW Data
    is collected.***


One can make sure whether data is collected or not by going into
directory where data is saved.

Once data is collected, we will move to next step by using one of the
two programs (GSA-ADA and RSV) fi

## 2. Analyzing data with GSA-ADA:

-   One can open this program by clicking **GSA-ADA.sav ** file that is
    in the folder in desktop.
-   It popups a new window named **“Image format and size”** where we
    define the image format.  For PE detector, it **TIFF an size
    1024x1024 pixel**.  Therefore select **“Tiff”**and correct size
    here.  Then, hit **“start”**.
-   It opens another window named **“GSA-ADA.ver1.6 September 7 2012”**.
-   In this program, open one of the file in the directory where data
    collected by selecting **FileOpen**.  

Check the orientation of the image by looking at the beam stop shadow
where it is pointing. 

 Image at 3ID-C PE detector is 90 degree rotated to reference and beam
stop should be seen in the horizontal plane pointing right to left.  

In reality it should point vertical from bottom to top.

-   For 3ID-C PE detector select **“Invert X, Invert Y, and Transpose”**
    all three on the upper right side of the window to bring orientation
    to what GSE-ADA can process (that is beam stop from pointing down)
-   Then reopen one of the images again.  Now one can sees that beam
    stop shadow is rotated vertically and shown from bottom. 
-   Then go to **“SCAN”**in the menu bar and click **“Merge step
    images”** bottom on the lower right side.  Program goes through all
    images to merge them.
-   One can change the range of colors for easy view of weak peaks say
    from 100010000.
-   At this point, one should make sure that proper calibration values
    are obtained and ready for use.  

This is under main menu named **“Calibration”.**  Calibration files are
created by diffraction image from standard CeO2 powder.  This data
should be taken before the sample images or usually there should be
calibration file named **“cal.cal”** already taken before.  

Unless detector position did not changed or detector is not removed,
this will not change and one can use this file.  

One can open this file under **“Calibration”, Open and opening correct
xxx.cal file.  **

One can check calibration and so on by selecting **“Show rings”** in the
lower right side of the window.  

After this action, calibration rings will be overlaid on the image.  

Check whether everything is fine, If there is a problem like same set of
two theta points show themselves on the opposite side of the CeO2
rings.  Then just do the calibration again.

**Creating Calibration file using standard powder sample,**

-   Go to **FileOpen**and find calibration file.
-   Change signal to noise ratio to smaller number.  This is the field
    under **“TEST”** button on the lower right side of the
    **“Calibration”** window (like to value 1.1)
-   Then check **“Refine cal”** next to **“TEST”** button.  It takes
    about 30 second.  After it is done, it gives result with standard
    deviations.  Check this result,  If it is okay,
-   Then save the calibration file as ”xxx**.cal”** file.

Open again one of the collected data and merge again.  Verify
calibration as well.

**Peak search,**

-   Select **“SEARCH”** window next to File menu for peak search in the
    image.  

Even though, one can select diffraction peaks by hand, **GSA-ADA**
program can find diffraction peaks automatically.  This can be done by

-   Clicking “**PS button”.**Make sure output directory is same as the
    directory that you read the images.  

By clicking **PS** button, program starts searching merged image file
and shows progress in new pop up window. 

If program returns with results that are not realistic like many more
boxes than the existing peaks or half of the screen is full with boxes
but the other half is empty vs., change **Threshold (say 1.051.1. **  

-   Then go to **“PEAKS”** window and click **“CLEAR”** button.
-   Later go back to **“SEARCH”** window and change **“minI” from 10 to
    100 and “PS search”** again.  Remember Threshold and min I important
    values to change.  
-   At the end, program finds most of the peaks.  Some might not be
    found or some of them might be wrong.  

In the program, there is an option to add or remove peaks manually. 

In order to use this feature, drag mouse in to image and perform right
click.  It will bring drop menu and select **“ADD peak”**.** **

Unfortunately, one can add one peak at a time.  

Then drag mouse over the peak.  Peak will be highlighted by a box.  

Perform this until you add all the peaks.  

One can also remove unwanted peaks in the program by clicking right
mouse and selecting **“Select”**. 

Then select the boxes that are going to be removed with clicking left
mouse and dragging mouse over the boxes/region and clicking left mouse
again.  

In this way, one selects the unwanted peaks for removing purposes.  

Then click **“DELETE”** button on the right top side of the **PEAK**
menu. 

You can turn of selection by clicking right mouse in the image window by
selecting **“SELECTION OFF”**.  Note, this peak search routine creates a
file named **“a.pks”** after performing search.

-   Now peak selection is done and ready for fitting.  

Before performing fitting, one can check the diffraction peaks and
selection of boxes around these peaks for the last time. 

Fitting is done in boxes and box size is measured in pixels. 

The number in the field **“box”** is radius of the box.  Change box size
**from 20 to 10** since 20 is too big (box size 10 means, box is chosen
10 pixels on the left and right side).  

Click **“Change size”** just underneath.  

There are for windows with three of them are in black color and one of
them (lower right corner) has information regarding peaks.  

One can check the individual peaks by selecting one of them and
scrolling down of each.  

These three windows show the magnified image of the diffraction peaks
and once scrolled, main image window shows selected peak box with green
color.  

Therefore, one can check the quality of the peak this way.  

Keep scrolling to different peaks; if diffraction is just one pixel, you
can delete it by clicking **“delete”** on the top left side in
**PEAK**menu.  Also if it gives some error message remove that point as
well.  

After surveying and removing unwanted peaks, then save file into same
file by clicking to **”SAVE”** and this will popup save window.  Save to
same file as named **“a.pks”.**

-   Now, we have pixel coordinate of the peaks we find and we need to
    know the angles at which the peak had max intensity.  Therefore,
    this is one of the important steps.  

For this step, go to **“SCAN”** window and tell the program how the scan
was done.  

We did our scan **“START” at -15 degree with “STEP” of 1.** 

(When we open the first image at the beginning, the program already
found out that we have”**number Images” 30** with **“Start no” 1.)**

After checking all these fields, make sure everything is okay, then
click **“COMPUT> FROM SCAN”** button.  
This opens the images in sequence of how intensity varied.  

It gives message that profile computation is successfully completed.  

When it is done program gives output (that is in the **peak** menu) of
angles in the column last to second. 

After we finished analyzing steps, we have to save the file again in
**a.pks** file.

## 3. Extracting orientation matrix by RSV utility.

Now that we determine the pixel coordinate of the peak as well as the
angles associated with those peaks, we are ready for calculating and
refining the lattice parameters and orientation matrix of the single
crystal.

For this, we will use second program called **RSV.**
-   Open **a.pks**file under **FILE Open. **
-   In the view window, program shows the projection of the reciprocal
    space along the x-ray direction of the each of the diffraction peaks
    that we used. We can change the scaling and rotation of the viewing
    angle to investigate the profile.
-   This rotation can be done by selecting **“HAND ROTATION”**. 

It rotates the reciprocal space image around and one can look for how
these diffraction points are aligned along a line.  

In good fitting diffraction points should perfectly align to lines.

Then we should be able to index it.  

-   Next go to **“INDEX”** and **“TRANSFORM”** .  

There is an external program called **“CELLNOW”**.  Click this and it
says current peak table has been saved in the file named **“xxx.php”**. 
Say OK.

This the way it passes the information to **cellnow**. Save it in an
input file that has extension **.p4p**  

Pops up new window.

-   First thing **CELLNOW** ask in **cell-now.exe** window is the name
    of the file type **xxx.p4p**
-   Then, it asks some questions, hit enter until program ask **min and
    max values allowed cell edges.  2-10 is fine.  Hit enter again.**
-   CELLNOW program comes with possible solutions.  Select the solution
    that you want.
-   Then it asks a name for output file like **“1.p4p”. **The default
    directory for this file i_m** 
-   You can read this calcultd orientation matrix in the main program
    by going to **“INDEX””FILE” and click on “READ from p4p” in the
    directory specif_m1.p4p** .  
After we open this file, program displays the lattice parameters that
contain the file.

-   There is a button named **“SELECT w/UB”**, if we click it, we can
    see colors of each point changes.

Calculated values are off from integer number about 0.1, it is selected
with darker color and not indexable.

Go to **View and click Delete selected** to remove them.

-   Go to **REFINE**and impose the symmetry constrain like tetragonal.
-   Then click **REFINE w/d space** and it shows **hkl values.**
-   One can check under **FILTER** distributions of error for difference
    of d-spacing calculated for each peak from the hkl orientation
    matrix versus what was measured.  Some of the outliers might be
    big. 

We have orientation matrix that we should share.

-   Under **INDEX FILE, SAVE in UB format** called **amb.U
-   Go back to **GSE-ADA** program and **PREDICTSIMULATE** opens new
    window called diffraction image **simulation/ manual. Indexing** 
-   Lets merge the image again to see all the peaks under **SCANMERGE
    STEP Image.** 
-   Then in extra window, click **OPEN and and open “amb.UB” file**
-   There is an opening angle of DAC (select this angle, if no DAC use
    say 180 degree)
-   Then click **“GENERATE”**should calculate where peaks should be.
-   In program, there is a virtual goniometer that one can simulate what
    will happen or how much Chi angle should be ratated to bring desired
    peak to horizontal axis so on.

Select **Chi angle in say 5degree step and then click chi.**  This might
be very useful tool to see.

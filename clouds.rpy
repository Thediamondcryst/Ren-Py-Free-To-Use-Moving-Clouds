##########################################################################
###
###
### Woo! New Open sourced system!
###
### This time, it's clouds. Clouds are a way to add animations to backgrounds. It's small, but a nice detail to add to backgrounds.
### 
### This project includes 7 clouds in 3 different versions: Day, Sunset/Sunrise and Night. All clouds are free to use, free to edit, and free to add new ones.
### Any new clouds should follow the flat and intentional art style, meant to work with any or most backgrounds. 
###
###
###
### If you're making new clouds:
###
### Day clouds versions features a white base (#FFFFFF), with a light blue midground (#eaf6fc), and a blue-ish foreground (#b4d7f7).
###
### Sunset clouds versions features a blue grey-ish base (#646478), with a darker blue grey-ish midground (#5b5f75), and a dark blue grey-ish foreground (#495371).*
### Or, add a black (#000000) Color Overlay effect with the Darken blending mode to the Day clouds and set it set to 60% opacity, and another Color Overlay to it set as Drk Blue (#101055) with the Color blending mode set to 30% opacity.*
### This should works with darker sunset images, especially near the sky above the sun, where it's slowly getting to night time.
### 
### Night clouds versions features a dark blue grey-ish base (#27263a), with a darker dark blue grey-ish midground (#25263a), and a darker darker dark blue grey-ish foreground (#20233a).*
### Or, add a really dark blue (#100f25) Color Overlay effect with the Darken blending mode to the Day clouds and set it to 90% opacity.*
###
### *Note: These colors were made to work with Daring Academy, so it may not work with all games. But, since this is open source, feel free to edit them and add the to the project.
###        Just, don't edit those in "images/clouds/daring_academy_clouds/", since it would break compatibility with the game when upgrading. Thanks!
###
###
###
### If you use this system, feel free to credit "Thediamondcrystal" in your game's credits. (But, it's not required. I just wanted to make moving clouds in Daring Academy, and decided to gift this to anyone!)
###
###
###
### Anyways, thank you to anyone who uses this system, and enjoy moving clouds!
###
###
##########################################################################


##########################################################################
###
### These are the defines for the clouds.
### Each clouds drawn should be placed in "images/clouds/" and either "day/" for day/normal clouds, "sunset/" for sunset/sunrise clouds or "night" for night clouds.
###
### Always make sure to check the github to check if there's ever new clouds.
###
##########################################################################


image clouds_images_day:
    renpy.random.choice(
        ["images/clouds/day/large_cloud_1.png",
        "images/clouds/day/large_cloud_2.png",
        "images/clouds/day/small_cloud_1.png",
        "images/clouds/day/small_cloud_2.png",
        "images/clouds/day/medium_cloud_1.png",
        "images/clouds/day/medium_cloud_2.png",
        "images/clouds/day/heart_cloud_1.png"
        ]
    )

image clouds_images_sunset:
    renpy.random.choice(
        ["images/clouds/sunset/large_cloud_sunset_1.png",
        "images/clouds/sunset/large_cloud_sunset_2.png",
        "images/clouds/sunset/small_cloud_sunset_1.png",
        "images/clouds/sunset/small_cloud_sunset_2.png",
        "images/clouds/sunset/medium_cloud_sunset_1.png",
        "images/clouds/sunset/medium_cloud_sunset_2.png",
        "images/clouds/sunset/heart_cloud_sunset_1.png"
        ]
    )

image clouds_images_night:
    renpy.random.choice(
        ["images/clouds/night/large_cloud_night_1.png",
        "images/clouds/night/large_cloud_night_2.png",
        "images/clouds/night/small_cloud_night_1.png",
        "images/clouds/night/small_cloud_night_2.png",
        "images/clouds/night/medium_cloud_night_1.png",
        "images/clouds/night/medium_cloud_night_2.png",
        "images/clouds/night/heart_cloud_night_1.png"
        ]
    )



##########################################################################
###
### The following codes are for the moving clouds effect, and should 𝗡𝗢𝗧 be edited, except the "count" number if you think it's too any clouds, or too little.
###
### The code includes 3 amount types: Low, Normal and High. Each adds 25 clouds to the screen. It also has 3 different time versions: Day, Sunset/Sunrise and Night.
###
### As said previously, do 𝗡𝗢𝗧 edit the code here, or crazy stuff might happen.
###
##########################################################################


# Low Clouds Amount
image clouds_blossom_low_day:
    SnowBlossom("clouds_images_day", count=25, border=340, xspeed=(60, 30), yspeed=(0, 0), start=20, fast=False, horizontal=True)

image clouds_blossom_low_sunset:
    SnowBlossom("clouds_images_sunset", count=25, border=340, xspeed=(60, 30), yspeed=(0, 0), start=20, fast=False, horizontal=True)

image clouds_blossom_low_night:
    SnowBlossom("clouds_images_night", count=25, border=340, xspeed=(60, 30), yspeed=(0, 0), start=20, fast=False, horizontal=True)


# Normal Clouds Amount
image clouds_blossom_day:
    SnowBlossom("clouds_images_day", count=50, border=340, xspeed=(60, 30), yspeed=(0, 0), start=20, fast=False, horizontal=True)

image clouds_blossom_sunset:
    SnowBlossom("clouds_images_sunset", count=50, border=340, xspeed=(60, 30), yspeed=(0, 0), start=20, fast=False, horizontal=True)

image clouds_blossom_night:
    SnowBlossom("clouds_images_night", count=50, border=340, xspeed=(60, 30), yspeed=(0, 0), start=20, fast=False, horizontal=True)


# High Clouds Amount
image clouds_blossom_high_day:
    SnowBlossom("clouds_images_day", count=75, border=340, xspeed=(60, 30), yspeed=(0, 0), start=20, fast=False, horizontal=True)

image clouds_blossom_high_sunset:
    SnowBlossom("clouds_images_sunset", count=75, border=340, xspeed=(60, 30), yspeed=(0, 0), start=20, fast=False, horizontal=True)

image clouds_blossom_high_night:
    SnowBlossom("clouds_images_night", count=75, border=340, xspeed=(60, 30), yspeed=(0, 0), start=20, fast=False, horizontal=True)




##########################################################################
###
### The following codes are the actual images you should add to your backgrounds.
###
### The code includes 3 amount types: Low, Normal and High. Each adds 25 clouds to the screen. It also has 3 different time versions: Day, Sunset/Sunrise and Night.
###
### To add clouds to your background, create a new image as either a Composite() or a Fixed() image type, put your background color/image, put the clouds image name (clouds_low_day, clouds_high_night, etc), then add the rest of the background above.
###
### The code for the background should look like that:
###
### image sacred_heart_academy_front_day = Composite( # This is the image define, and in this case, I used Composite(), but fixed could also be used without issues.
###     (1280, 720), # This is the size of the image.
###     (0, 0), Solid("00c3ff"), # This is the background, and in this case, it's a solid color, but can easily be an image if you change 𝗦𝗼𝗹𝗶𝗱("𝟬𝟬𝗰𝟯𝗳𝗳") to "𝗶𝗺𝗮𝗴𝗲_𝗽𝗮𝘁𝗵/𝗶𝗺𝗮𝗴𝗲_𝗻𝗮𝗺𝗲.𝗲𝘅𝘁𝗲𝗻𝘀𝗶𝗼𝗻".
###     (0, 0), "clouds_day",
###     (0, 0), "images/background/school/overlay/sacred_heart_academy_front_overlay_day.png",
###     )
###
##########################################################################


# Low Clouds Amount
image clouds_low_day:
    "clouds_blossom_low_day"
    # xysize (1280, 300)
    ypos -200
    # yoffset 200

image clouds_low_sunset:
    "clouds_blossom_low_sunset"
    # xysize (1280, 600)
    ypos -200
    # yoffset 200

image clouds_low_night:
    "clouds_blossom_low_night"
    # xysize (1280, 600)
    ypos -200
    # yoffset 200



# Normal Clouds Amount
image clouds_day:
    "clouds_blossom_day"
    # xysize (1280, 300)
    ypos -200
    # yoffset 200

image clouds_sunset:
    "clouds_blossom_sunset"
    # xysize (1280, 600)
    ypos -200
    # yoffset 200

image clouds_night:
    "clouds_blossom_night"
    # xysize (1280, 600)
    ypos -200
    # yoffset 200



# High Clouds Amount
image clouds_high_day:
    "clouds_blossom_high_day"
    # xysize (1280, 300)
    ypos -200
    # yoffset 200

image clouds_high_sunset:
    "clouds_blossom_high_sunset"
    # xysize (1280, 600)
    ypos -200
    # yoffset 200

image clouds_high_night:
    "clouds_blossom_high_night"
    # xysize (1280, 600)
    ypos -200
    # yoffset 200
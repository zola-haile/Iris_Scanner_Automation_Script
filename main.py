import pexpect
import csv
import os
import re


from skimage.metrics import structural_similarity as ssim
import argparse
import imutils
import cv2




firstTime=input("Is this your first run(y/n): ")

if firstTime.lower()=='y':
    #If this is the first run, uncomment the following two lines
    from nameReader import nameList,nameList2


elif firstTime.lower()=='n':
    #If not first run, uncomment the following:
    os.system("python3 /Users/czajkademo1/Desktop/pyDemo/name_to_be_scanned.py")
    from name_to_be_scanned import nameList,nameList2



#image name used for naming
imgName=nameList

# #image name used for checking similarity

# nameList=nameList2



def expect_and_send(sendValue):
    child.expect("Enter your choice: ")
    child.sendline(sendValue)


# *****************#########$$$$$$$$$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# *****************#########$$$$$$$$$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#               Main process
# *****************#########$$$$$$$$$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# ******************#########$$$$$$$$$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



# Set the environment variable
os.environ['DYLD_LIBRARY_PATH'] = '/opt/IriTech/IDDK-2000-3.3.1-OSX/demo/source:' + os.environ.get('DYLD_LIBRARY_PATH', '')

# Path to the executable
executable = '/opt/IriTech/IDDK-2000-3.3.1-OSX/demo/source/Iddk2000Demo'

loop=True


list_of_unscanned_iris=[]
number_imgs_taken=0
while loop:

    # Start the process
    child = pexpect.spawn(executable)
    child.logfile = open('pexpect.log', 'wb')

    # Interact with the process
    child.expect("Please press ENTER to continue ...")
    child.sendline("")

    # Reset on open device: 
    #   1. Yes (default)
    #   2. No

    expect_and_send("1")

    # MAIN MENU: Select one of the features below
    #   1. Login
    #   2. Logout
    #   3. Device Management
    #   4. Device & SDK Information
    #   5. Capturing Process
    #   6. Iris Recognition
    #   7. Power Management
    #   8. Recovery (IriShield USB only)
    #   9. Exit
    # Enter your choice:


    expect_and_send("5")


    # Parameters for capturing process
    # Capture mode: 
    #   1. IDDK_TIMEBASED (default) 
    #   2. IDDK_FRAMEBASED
    # Enter your choice: 


    expect_and_send("1")


    # Enter the duration since iris detected (from 1 to 600 seconds, enter for 3): 5

    child.expect(r"Enter the duration since iris detected \(from 1 to 600 seconds, enter for 3\): ")
    child.sendline("5")

    # Quality mode: 
    #   1. Normal (default)
    #   2. High 
    #   3. Very High
    # Enter your choice:

    expect_and_send("3")

    # Enable auto led? 
    #   1. Yes (default)
    #   2. No
    # Enter your choice:


    expect_and_send("1")

    child.expect("Put your eyes in front of the camera")
    print("""Put your eyes in front of the camera
        Scanning for eyes............................""")

    # Simulate waiting for the eye scanning process
    
    loop_to_capture=True
    count=0


    while loop_to_capture:

        index=child.expect(["Error: IDDK_SE_NO_QUALIFIED_FRAME","Error: IDDK_SE_NO_FRAME_AVAILABLE","Do you want to get the result image?"])
        
        if index==0 or index==1:

            # MAIN MENU: Select one of the features below
            #   1. Login
            #   2. Logout
            #   3. Device Management
            #   4. Device & SDK Information
            #   5. Capturing Process
            #   6. Iris Recognition
            #   7. Power Management
            #   8. Recovery (IriShield USB only)
            #   9. Exit
            # Enter your choice:

            expect_and_send("5")

            # Parameters for capturing process
            # Capture mode: 
            #   1. IDDK_TIMEBASED (default) 
            #   2. IDDK_FRAMEBASED
            # Enter your choice: 

            expect_and_send("1")

            # Enter the duration since iris detected (from 1 to 600 seconds, enter for 3): 5

            child.expect(r"Enter the duration since iris detected \(from 1 to 600 seconds, enter for 3\): ")
            child.sendline("5")

            # Quality mode: 
            #   1. Normal (default)
            #   2. High 
            #   3. Very High
            # Enter your choice:

            expect_and_send("2")

            # Enable auto led? 
            #   1. Yes (default)
            #   2. No
            # Enter your choice:


            expect_and_send("1")

            child.expect("Put your eyes in front of the camera")

            print("""Put your eyes in front of the camera
                Scanning for eyes............................""")

            
            loop_to_capture=True
            count+=1
            if count==5:
                # MAIN MENU: Select one of the features below
            #   1. Login
            #   2. Logout
            #   3. Device Management
            #   4. Device & SDK Information
            #   5. Capturing Process
            #   6. Iris Recognition
            #   7. Power Management
            #   8. Recovery (IriShield USB only)
            #   9. Exit
            # Enter your choice:

                expect_and_send("9")

                list_of_unscanned_iris.append(imgName[0])


                with open("unscanned_imgName.csv",'a', newline='') as csvfile:
                    csvwriter=csv.writer(csvfile)

                    csvwriter.writerows(imgName[0])


                print("****  This iris could not be scanned, so it is skiped ***")
                break


            continue

        elif index==2:
            loop_to_capture=False



    # Do you want to get the result image? 
    #   1. No (default)
    #   2. Yes
    # Enter your choice: 2
    if index==2:
        expect_and_send("2")

        # Select image kind: 
        #   1. Original Image - K1 (default) 
        #   2. VGA Image - K2 
        #   3. Cropped Image - K3
        #   4. Cropped and Masked Image - K7
        # Enter your choice:

        expect_and_send("1")

        # Select image format: 
        #   1. Mono JP2 Image (default)
        #   2. Mono Raw Image
        #   3. IriTech JP2 Image
        #   4. IriTech Raw Image
        # Enter your choice: 1

        expect_and_send("1")

        # Enter compress ratio (enter for default): 50

        child.expect("Enter compress .*: ")
        child.sendline("50")

        # Do you want to get result ISO image: 
        #   1. No (default)
        #   2. Yes
        # Enter your choice:

        expect_and_send("1")


        # #Try another capture?
        #     # 	1. Yes (default)
        #     # 	2. No
        #     # Enter your choice: 2

        # expect_and_send("2")

        # #   MAIN MENU: Select one of the features below
        # # 	1. Login
        # # 	2. Logout
        # # 	3. Device Management
        # # 	4. Device & SDK Information
        # # 	5. Capturing Process
        # # 	6. Iris Recognition
        # # 	7. Power Management
        # # 	8. Recovery (IriShield USB only)
        # # 	9. Exit
        # # Enter your choice: 6

        # expect_and_send("6")

        # #         IRIS RECOGNITION: Please select one menu item 
        # # 	1. Main Menu
        # # 	2. Get Gallery Information
        # # 	3. Enroll Captured Iris
        # # 	4. Get Result Template
        # # 	5. Enroll Template
        # # 	6. Unenroll Templates
        # # 	7. Matching
        # # 	8. Exit
        # # Enter your choice: 7

        # expect_and_send("7")


        # #         Select the kind of comparison: 
        # # 	1. Compare11 (default)
        # # 	2. Compare1N
        # # 	3. Compare11WithTemplate
        # # Enter your choice: 1

        # expect_and_send("1")

        # # Enter the enrollee ID (less than 32 characters): 

        # child.expect("Enter the enrollee ID (less than 32 characters): ")
        # child.sendline(imgName[0])

        # # Regular expression to find the distance value
        # match = re.search(r'Compare Distance = (\d+\.\d+)', output)
        # if match:
        #     distance_wanted=float(match.group(1))
        #     print(distance_wanted)
        
        # Close the log file
        
        
        child.logfile.close()
    




    # *****************#########$$$$$$$$$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    #               checks the similarity between captured and original
    # *****************#########$$$$$$$$$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


        # captured_image_path = "/opt/IriTech/IDDK-2000-3.3.1-OSX/demo/source/UnknownEyeImage_1.jp2"
        # original_image = f"/Users/czajkademo1/Desktop/pyDemo/check_similarity/CrossImages/{nameList[0]}"

        # imageA = cv2.imread(captured_image_path)    
        
        # imageB = cv2.imread(original_image)
        
        # # convert the images to grayscale
        # grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
        # grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)# compute the Structural Similarity Index (SSIM) between the two
        # # images, ensuring that the difference image is returned
        # (score, diff) = ssim(grayA, grayB, full=True)
        # print(score)
        # diff = (diff * 255).astype("uint8")
        

        # if score<0.9:

        child=pexpect.spawn(f"mv /opt/IriTech/IDDK-2000-3.3.1-OSX/demo/source/UnknownEyeImage_1.jp2 /Users/czajkademo1/Desktop/pyDemo/saved_images/{imgName[0]}.jp2")
        print("Process completed.")



    imgName.pop(0)
    # nameList.pop(0)
    
    
    number_imgs_taken+=1
    print(f"Number of images scanned so far {number_imgs_taken}.")
    do_continue=input("Enter q to quit; anything else to continue: ")
    if do_continue.lower()!="q":
        loop=True
    else:
        loop=False





fileName_imgName_comparison="imgName_comparison.csv"
fileName_imgName_naming="imgName_naming.csv"


with open(fileName_imgName_comparison,'w', newline='') as csvfile:
    csvwriter=csv.writer(csvfile)

    for item in nameList:
        csvwriter.writerow([item])


with open(fileName_imgName_naming,'w', newline='') as csvfile:
    csvwriter=csv.writer(csvfile)

    for item in imgName:
        csvwriter.writerow([item])




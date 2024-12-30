# LogoMaker
A Python-based project that allows users to generate logos based on a given prompt. It uses the Unsplash API to search for relevant images (such as logos or related graphics) based on the user's query. The text you input is then overlayed on the image to create a personalized logo, which is saved to your local machine.

Features

Generate Logos: Enter a prompt (e.g., "government logo") and generate a logo by combining relevant images from Unsplash with custom text.


Customizable Text: Add any text to the logo that you want, such as a company name, tagline, or other branding text.


Download and Save: Generate logos and save them to a specified directory on your computer.


Make sure you have the following installed:
Python 3.x (Preferably the latest version)
Pip (Python's package installer)
Required Python Libraries:
Pillow (for image manipulation)
Requests (for making API requests)



You can install the required libraries by running the following commands:


#bash
pip install pillow requests
Get Unsplash API Key
Go to Unsplash Developer.
Log in or create a free Unsplash account.
Create a new application to get your API Access Key.
Copy the Access Key and use it in the code where instructed.



How to Use


1. Clone the Repository
#bash
git clone https://github.com/shannu-afk/logo-maker.git
cd logo-maker


2. Configure the Script
In the project folder, find the script file (e.g., logo_maker.py), and follow these steps:
Replace YOUR_UNSPLASH_ACCESS_KEY with the API key you obtained from Unsplash.



3. Run the Script

In your terminal, run the Python script:
#bash
python logo_maker.py
When prompted, enter:
The search query for the type of logo you want (e.g., "government logo").

The text you want to display on the logo (e.g., "My Company").
The script will fetch an image based on the query from Unsplash, overlay your custom text, and save the resulting logo in the output/ directory.

Example Prompt



#bash
Enter your prompt (e.g., 'government logo'): government logo
Enter the text for the logo (e.g., 'My Company'): My Company
The generated logo will be saved in the output/ directory.
Customization


You can easily customize the following aspects of the logo creation process:



Font Style and Size: Modify the font style and size for the text to fit your design. The script uses a default font, but you can specify a custom one (make sure it's available on your system).
Text Position: You can change the placement of the text on the image by adjusting the x_pos and y_pos variables.
Image Source: Currently, the script uses the Unsplash API to fetch images, but you can switch to other image APIs like Pexels or Pixabay by modifying the image search function.
Troubleshooting
API Rate Limiting: Unsplash allows 50 requests per hour on the free tier. If you exceed this limit, wait for the rate limit to reset, or upgrade to a paid plan for more requests.
No Images Found: If the search doesn't return any results, try using a more specific or different keyword.
Font Issues: If the default font doesn't work on your system, you can replace it with any other font file that’s available, or use a built-in font.
License
This project is licensed under the MIT License - see the LICENSE file for details.




Project Structure

logo-maker/

├── output/                   # Folder where generated logos are saved

├── logo_maker.py             # Main Python script for logo creation

├── requirements.txt          # List of Python libraries to install

└── README.md                 # This file

#Conclusion
This Logo Maker project allows you to quickly generate logos using high-quality images from Unsplash, adding custom text for personalization. It's easy to set up and modify to suit your needs, and you can use the free API tier for low-traffic applications.
Let me know if you need any further help with setup or customization!

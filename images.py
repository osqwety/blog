import os
import re
import shutil

# Paths (using raw strings to handle Windows backslashes correctly)
posts_dir = r"C:\Users\lambo\Documents\Obsidian_Vault\posts"
attachments_dir = r"C:\Users\lambo\Documents\Obsidian_Vault\images"
static_images_dir = r"C:\Users\lambo\Documents\blog\static\images"

# Step 1: Process each markdown file in the posts directory
for filename in os.listdir(posts_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(posts_dir, filename)
        
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
            print(content)
        
        # Step 2: Find all image links in the format ![Image Description](/images/Pasted%20image%20...%20.png)
        images = re.findall(r'\[\[([^]]*\.png)\]\]', content)
        print(images)
        
        # Step 3: Replace image links and ensure URLs are correctly formatted
        for image in images:
            # Prepare the Markdown-compatible link with %20 replacing spaces
            markdown_image = f"![Image Description]({image.replace(' ', '%20')})"
            print(markdown_image)
            content = content.replace(f"[[{image}]]", markdown_image)
            
            # Step 4: Copy the image to the Hugo static/images directory if it exists
            
            image_source = os.path.join(r"C:/Users/lambo/Documents/Obsidian_Vault", image)
            image_source = image_source.replace(' ', '%20')
            image_source = image_source.replace("..", "")
            print(image_source)
            if image_source == "":
                print("blank")
            print(f"yes: {image_source}")
            if os.path.exists(image_source):
                shutil.copy(image_source, static_images_dir)

        # Step 5: Write the updated content back to the markdown file
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)

print("Markdown files processed and images copied successfully.")

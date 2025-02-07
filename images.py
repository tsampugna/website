#import os
#import re
#import shutil

# # Paths (using raw strings to handle Windows backslashes correctly)
# posts_dir = r"C:\Users\Tony\Documents\sampugnablog\content\posts"
# attachments_dir = r"D:\Obsidian\Posts\attachments"
# static_images_dir = r"C:\Users\Tony\Documents\sampugnablog\static\images"

# # Step 1: Process each markdown file in the posts directory
# for filename in os.listdir(posts_dir):
    # if filename.endswith(".md"):
        # filepath = os.path.join(posts_dir, filename)
        
        # with open(filepath, "r", encoding="utf-8") as file:
            # content = file.read()
        
        # # Step 2: Find all image links in the format ![Image Description](/images/Pasted%20image%20...%20.png)
        # images = re.findall(r'\[\[([^]]*\.png)\]\]', content)
        
        # # Step 3: Replace image links and ensure URLs are correctly formatted
        # for image in images:
            # # Prepare the Markdown-compatible link with %20 replacing spaces
            # markdown_image = f"![Image Description](/images/{image.replace(' ', '%20')})"
            # content = content.replace(f"[[{image}]]", markdown_image)
            
            # # Step 4: Copy the image to the Hugo static/images directory if it exists
            # image_source = os.path.join(attachments_dir, image)
            # if os.path.exists(image_source):
                # shutil.copy(image_source, static_images_dir)

        # # Step 5: Write the updated content back to the markdown file
        # with open(filepath, "w", encoding="utf-8") as file:
            # file.write(content)

# print("Markdown files processed and images copied successfully.")



import os
import re
import shutil
import urllib.parse  # For decoding %20 in the image path

def process_markdown_images(md_dir, src_dir, dest_dir):
    """Processes all markdown files in a directory, updates image paths, and moves images."""

    # Ensure destination directory exists
    os.makedirs(dest_dir, exist_ok=True)

    # Regex pattern to find image links ![](path/to/image.jpg)
    image_pattern = re.compile(r'!\[(.*?)\]\((.*?)\)')

    # Process each markdown file in the directory
    for filename in os.listdir(md_dir):
        if filename.endswith(".md"):
            md_path = os.path.join(md_dir, filename)

            # Read the Markdown file
            with open(md_path, 'r', encoding='utf-8') as file:
                content = file.read()

            def update_image_link(match):
                """Replaces old image links with new ones and moves the image."""
                alt_text, old_path = match.groups()

                # Decode URL-encoded characters (e.g., %20 -> space)
                decoded_path = urllib.parse.unquote(old_path)

                # Replace spaces with hyphens in the filename
                filename_only = os.path.basename(decoded_path).replace(" ", "-")

                # New image path with leading '/'
                new_path = f"/images/{filename_only}"

                # Move the image to the new destination directory
                src_image_path = os.path.join(src_dir, decoded_path)
                dest_image_path = os.path.join(dest_dir, filename_only)

                # Ensure the image exists in the source directory
                if os.path.exists(src_image_path):
                    shutil.copy2(src_image_path, dest_image_path)
                    print(f"✅ Copied: {src_image_path} -> {dest_image_path}")
                else:
                    print(f"⚠️ Warning: Image not found: {src_image_path}")

                # Return updated Markdown image link
                return f"![{alt_text}]({new_path})"

            # Replace old image paths with new ones
            updated_content = image_pattern.sub(update_image_link, content)

            # Save updated Markdown file
            with open(md_path, 'w', encoding='utf-8') as file:
                file.write(updated_content)

            print(f"✅ Updated Markdown file: {md_path}")

# === CONFIGURATION ===
md_dir = r"C:\Users\Tony\Documents\sampugnablog\content\posts"  # Folder containing Markdown files
src_dir = r"D:\Obsidian\Posts\attachments"  # Folder where images are currently located
dest_dir = r"C:\Users\Tony\Documents\sampugnablog\static\images"  # New folder for images

# Run script
process_markdown_images(md_dir, src_dir, dest_dir)
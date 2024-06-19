import os

# Path to your directory containing images
img_dir = 'img/Taskify/'

# Function to generate HTML template for each image file
def generate_html_template(filename):
    img_path = os.path.join(img_dir, filename)
    img_name, img_ext = os.path.splitext(filename)
    portfolio_text = img_name.replace('-', ' ').title()  # Example transformation
    data_caption = img_name.title()  # Example transformation
    
    template = f'''
    <div class="col-lg-4 col-md-6 col-sm-12 portfolio-item pm wow fadeInUp" data-wow-delay="0.2s">
        <div class="portfolio-wrap">
            <div class="portfolio-img">
                <img src="{img_path}" alt="{img_name} Image"
                    class="img-fluid clickable-image" data-toggle="modal" data-target="#imageModal"
                    data-img-src="{img_path}" data-caption="{data_caption}">
            </div>
            <div class="portfolio-text">
                <h3>{portfolio_text}</h3>
            </div>
        </div>
    </div>
    '''
    return template.strip()

# List all files in the directory
files = os.listdir(img_dir)

# Generate templates for each file
a = 0
for file in files:
    if file.lower().endswith('.png') or file.lower().endswith('.jpg') or file.lower().endswith('.jpeg'):
        html_template = generate_html_template(file)
        print(html_template)
        print('\n')
        a = a + 1
print(a)

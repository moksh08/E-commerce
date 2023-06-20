# Django Project Documentation

## Description
This documentation provides an overview of the Django project developed for the CIA assignment. The project aims to [provide a brief description of the project's purpose or goal].

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
   - [Main Functions](#main-functions)
   - [Functionalities](#functionalities)
   - [User-Defined Functions](#user-defined-functions)
3. [Running the Project](#running-the-project)
4. [Function Outputs](#function-outputs)

## Installation<a name="installation"></a>
To set up the Django project, follow the steps below:

1. Clone the repository from GitHub:
   ```bash
   git clone <repository_url>
   ```

2. Install the required dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

## Usage<a name="usage"></a>

### Main Functions<a name="main-functions"></a>
The Django project includes the following main functions:

1. **product_list(request)** - [Renders a list of products]
   - Syntax:
    def product_list(request):
      products = Product.objects.all()
      return render(request, 'myapp/product_list.html', {'products': products})


2. **product_detail(request, pk)** - [Renders the details of a specific produc]
   - Syntax:
  def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'myapp/product_detail.html', {'product': product})
    
3. **add_product(request)** - [Handles the form submission to add a new product]
   - Syntax:
  def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'myapp/product_detail.html', {'product': product})




### Functionalities<a name="functionalities"></a>
The Django project provides the following functionalities:

1. **Displaying Product List1** - [This functionality displays a list of all products available]

**Steps:**
   1.Retrieves all products from the database using the Product.objects.all() method.
   2.Renders the product_list.html template and passes the retrieved products to it.

2. **Viewing Product Details** - [This functionality displays the details of a specific product]

**Steps:**
   1.Retrieves the product with the given primary key (pk) from the database using the get_object_or_404() function.
   2.Renders the product_detail.html template and passes the retrieved product to it.
  
3. **Adding a Product** - [This functionality allows users to add a new product to the database through a form submission]

**Steps:**
   1.Checks if the request method is POST.
   2.If it is POST, creates a new Product object and populates its attributes with the form data.
   3.Saves the new product to the database.
   4.Redirects the user to the homepage.
   5.If the request method is not POST, renders the add_product.html template.


### User-Defined Functions<a name="user-defined-functions"></a>
The Django project includes the following user-defined functions:

1. **user_directory_path(instance, filename)** - [This function defines the path where uploaded product images will be stored in the server filesystem.]
   - Syntax:
      def user_directory_path(instance, filename):
         return '{0}/{1}'.format("product_photos", filename)


2. **str(self)** - [his function provides a string representation of the Product model.]
   Syntax:
      def __str__(self):
         return self.name



## Running the Project<a name="running-the-project"></a>
To run the Django project locally, perform the following steps:

1. Navigate to the project directory:
   ```bash
   cd <myproject>
   ```

2. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

3. Start the development server:
   ```bash
   python manage.py runserver
   ```

4. Access the project in a web browser at `http://localhost:8000/`.


## Function Outputs<a name="function-outputs"></a>
This section provides the expected output for the main functions and user-defined functions:

### Main Function Outputs
1. **Function: product_list(request)** 
Example Output: The product_list function renders the product_list.html template and passes a dictionary containing the products to the template for rendering.

2. **Function: product_detail(request, pk)** 
Example Output: The product_detail function renders the product_detail.html template and passes a dictionary containing the product to the template for rendering.

2. **Function: add_product(request)** 
Example Output: Upon successful form submission, the function creates a new Product object with the provided information and saves it to the database. It then redirects the user to the homepage.



### User-Defined Function Outputs
1. **Function: user_directory_path(instance, filename)**
Example Output: If instance is an instance of the Product model and filename is "example.jpg", the function would return "product_photos/example.jpg".

2. **Function: str(self)** 
Example Output: If the name of the product is "Example Product", the function would return "Example Product".



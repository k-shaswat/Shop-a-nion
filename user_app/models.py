from django.db import models

# Create your models here.
class Category(models.Model):
	"""We use this for creating category table.

	It returns :func:`__str__ function`.

	.. note::

	   Django automatically converts it to :mod:`sqllite`.

	"""
	categoryName = models.CharField(max_length=50)
	def __str__(self):
		return f'{self.categoryName}'


class Product(models.Model):
	"""We use this for creating Product table with attributes like productBuyed,produductCategory,etc.

    It returns :func:`__str__ function`.

    .. note::

       Django automatically converts it to :mod:`sqllite`.

    """

	productImage = models.ImageField(upload_to = "productImages/")
	productName = models.CharField(max_length=40)
	productDescription = models.TextField()
	productViewed = models.IntegerField()
	productBuyed = models.IntegerField()
	productCompany = models.CharField(max_length=100)
	productPrice = models.IntegerField()
	productDiscount = models.IntegerField()
	productAddedDate = models.DateTimeField(auto_now_add=True)
	productQuantity=models.IntegerField()
	productDiscountedPrice=models.IntegerField()
	productCategory = models.ForeignKey(Category,on_delete=models.CASCADE)
	avgReview=models.FloatField(default=105)
	noOfReviews=models.IntegerField(default=1)
	def __str__(self):
		return f'{self.productName}'

class User(models.Model):
	"""We use this for creating User table with attributes like UserName,UserEamail,etc.

	It returns :func:`__str__ function`.

	.. note::

	   Django automatically converts it to :mod:`sqllite`.

	"""
	userName = models.CharField(max_length=40)
	userEmail = models.EmailField(max_length=60,unique=True)
	userPassword = models.CharField(max_length=20)
	userContact = models.CharField(max_length=20)
	userAddedDate = models.DateTimeField(auto_now_add=True)
	userProducts = models.ManyToManyField(Product,related_name="userProducts")
	userCart = models.ManyToManyField(Product,related_name="userCart")
	#userBuyedProducts=models.ManyToManyField(Product,related_name="userBuyedProducts")
	userAddress = models.CharField(max_length=200)
	def __str__(self):
		return f'{self.userName}'

class Review(models.Model):
	"""We use this for creating Review table with attributes like reviewTitle,reviewUseretc.

    It returns :func:`__str__ function`.

    .. note::

       Django automatically converts it to :mod:`sqllite`.

    """

	reviewTitle=models.CharField(max_length=40)
	reviewDesc=models.TextField()
	reviewRating=models.IntegerField()
	reviewUser=models.ForeignKey(User,on_delete=models.CASCADE)
	reviewProduct=models.ForeignKey(Product,on_delete=models.CASCADE)
	reviewAddedDate=models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return f'{self.reviewTitle} - {self.reviewTitle}'


STATUS_CHOICES = [
    ("Pending", "Pending"),
    ("Delivered", "Delivered"),
]
MODE_CHOICES = [
    ("Cash On Delivery", "Cash On Delivery"),
    ("Online Payment", "Online Payment"),
]
class Sales(models.Model):
	saleProducts=models.ManyToManyField(Product,related_name="saleProducts")
	saleUser=models.ForeignKey(User,on_delete=models.CASCADE)
	saleAddedDate = models.DateTimeField(auto_now_add=True)
	saleAddress = models.CharField(max_length=200)
	status = models.CharField(max_length=50, choices=STATUS_CHOICES)
	salePrice = models.IntegerField()
	paymentMode = models.CharField(max_length=50, choices=MODE_CHOICES)
	razorpay_order_id = models.CharField(max_length=200,default='None')
	razorpay_payment_id = models.CharField(max_length=200,default='None')
	razorpay_signature =  models.CharField(max_length=500,default='None')
	def __str__(self):
		return f'{self.saleUser}'

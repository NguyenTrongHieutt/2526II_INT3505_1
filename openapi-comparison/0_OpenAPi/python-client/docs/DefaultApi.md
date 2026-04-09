# openapi_client.DefaultApi

All URIs are relative to *http://127.0.0.1:5000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_book_reviews_get**](DefaultApi.md#api_v1_book_reviews_get) | **GET** /api/v1/book-reviews | Get list of reviews
[**api_v1_book_reviews_post**](DefaultApi.md#api_v1_book_reviews_post) | **POST** /api/v1/book-reviews | Create review
[**api_v1_book_reviews_review_id_delete**](DefaultApi.md#api_v1_book_reviews_review_id_delete) | **DELETE** /api/v1/book-reviews/{review_id} | Delete review
[**api_v1_book_reviews_review_id_get**](DefaultApi.md#api_v1_book_reviews_review_id_get) | **GET** /api/v1/book-reviews/{review_id} | Get review by ID
[**api_v1_books_book_id_delete**](DefaultApi.md#api_v1_books_book_id_delete) | **DELETE** /api/v1/books/{book_id} | Delete book
[**api_v1_books_book_id_get**](DefaultApi.md#api_v1_books_book_id_get) | **GET** /api/v1/books/{book_id} | Get book by ID
[**api_v1_books_get**](DefaultApi.md#api_v1_books_get) | **GET** /api/v1/books | Get list of books
[**api_v1_books_post**](DefaultApi.md#api_v1_books_post) | **POST** /api/v1/books | Create new book
[**api_v1_users_get**](DefaultApi.md#api_v1_users_get) | **GET** /api/v1/users | Get list of users
[**api_v1_users_post**](DefaultApi.md#api_v1_users_post) | **POST** /api/v1/users | Create new user
[**api_v1_users_user_id_delete**](DefaultApi.md#api_v1_users_user_id_delete) | **DELETE** /api/v1/users/{user_id} | Delete user
[**api_v1_users_user_id_get**](DefaultApi.md#api_v1_users_user_id_get) | **GET** /api/v1/users/{user_id} | Get user by ID


# **api_v1_book_reviews_get**
> ReviewsResponse api_v1_book_reviews_get()

Get list of reviews

### Example


```python
import openapi_client
from openapi_client.models.reviews_response import ReviewsResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://127.0.0.1:5000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Get list of reviews
        api_response = api_instance.api_v1_book_reviews_get()
        print("The response of DefaultApi->api_v1_book_reviews_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->api_v1_book_reviews_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ReviewsResponse**](ReviewsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List reviews |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_book_reviews_post**
> ReviewResponse api_v1_book_reviews_post(review_input)

Create review

### Example


```python
import openapi_client
from openapi_client.models.review_input import ReviewInput
from openapi_client.models.review_response import ReviewResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://127.0.0.1:5000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    review_input = openapi_client.ReviewInput() # ReviewInput | 

    try:
        # Create review
        api_response = api_instance.api_v1_book_reviews_post(review_input)
        print("The response of DefaultApi->api_v1_book_reviews_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->api_v1_book_reviews_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **review_input** | [**ReviewInput**](ReviewInput.md)|  | 

### Return type

[**ReviewResponse**](ReviewResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_book_reviews_review_id_delete**
> api_v1_book_reviews_review_id_delete(review_id)

Delete review

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://127.0.0.1:5000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    review_id = 56 # int | 

    try:
        # Delete review
        api_instance.api_v1_book_reviews_review_id_delete(review_id)
    except Exception as e:
        print("Exception when calling DefaultApi->api_v1_book_reviews_review_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **review_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Deleted |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_book_reviews_review_id_get**
> ReviewResponse api_v1_book_reviews_review_id_get(review_id)

Get review by ID

### Example


```python
import openapi_client
from openapi_client.models.review_response import ReviewResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://127.0.0.1:5000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    review_id = 56 # int | 

    try:
        # Get review by ID
        api_response = api_instance.api_v1_book_reviews_review_id_get(review_id)
        print("The response of DefaultApi->api_v1_book_reviews_review_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->api_v1_book_reviews_review_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **review_id** | **int**|  | 

### Return type

[**ReviewResponse**](ReviewResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Review detail |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_books_book_id_delete**
> api_v1_books_book_id_delete(book_id)

Delete book

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://127.0.0.1:5000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    book_id = 56 # int | 

    try:
        # Delete book
        api_instance.api_v1_books_book_id_delete(book_id)
    except Exception as e:
        print("Exception when calling DefaultApi->api_v1_books_book_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **book_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Deleted |  -  |
**404** | Book not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_books_book_id_get**
> BookResponse api_v1_books_book_id_get(book_id)

Get book by ID

### Example


```python
import openapi_client
from openapi_client.models.book_response import BookResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://127.0.0.1:5000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    book_id = 56 # int | 

    try:
        # Get book by ID
        api_response = api_instance.api_v1_books_book_id_get(book_id)
        print("The response of DefaultApi->api_v1_books_book_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->api_v1_books_book_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **book_id** | **int**|  | 

### Return type

[**BookResponse**](BookResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Book detail |  -  |
**404** | Book not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_books_get**
> BooksResponse api_v1_books_get()

Get list of books

### Example


```python
import openapi_client
from openapi_client.models.books_response import BooksResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://127.0.0.1:5000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Get list of books
        api_response = api_instance.api_v1_books_get()
        print("The response of DefaultApi->api_v1_books_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->api_v1_books_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BooksResponse**](BooksResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of books |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_books_post**
> BookResponse api_v1_books_post(book_input)

Create new book

### Example


```python
import openapi_client
from openapi_client.models.book_input import BookInput
from openapi_client.models.book_response import BookResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://127.0.0.1:5000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    book_input = openapi_client.BookInput() # BookInput | 

    try:
        # Create new book
        api_response = api_instance.api_v1_books_post(book_input)
        print("The response of DefaultApi->api_v1_books_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->api_v1_books_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **book_input** | [**BookInput**](BookInput.md)|  | 

### Return type

[**BookResponse**](BookResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Book created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_users_get**
> UsersResponse api_v1_users_get()

Get list of users

### Example


```python
import openapi_client
from openapi_client.models.users_response import UsersResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://127.0.0.1:5000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Get list of users
        api_response = api_instance.api_v1_users_get()
        print("The response of DefaultApi->api_v1_users_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->api_v1_users_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UsersResponse**](UsersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List users |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_users_post**
> UserResponse api_v1_users_post(user_input)

Create new user

### Example


```python
import openapi_client
from openapi_client.models.user_input import UserInput
from openapi_client.models.user_response import UserResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://127.0.0.1:5000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user_input = openapi_client.UserInput() # UserInput | 

    try:
        # Create new user
        api_response = api_instance.api_v1_users_post(user_input)
        print("The response of DefaultApi->api_v1_users_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->api_v1_users_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_input** | [**UserInput**](UserInput.md)|  | 

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_users_user_id_delete**
> api_v1_users_user_id_delete(user_id)

Delete user

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://127.0.0.1:5000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user_id = 56 # int | 

    try:
        # Delete user
        api_instance.api_v1_users_user_id_delete(user_id)
    except Exception as e:
        print("Exception when calling DefaultApi->api_v1_users_user_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Deleted |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_users_user_id_get**
> UserResponse api_v1_users_user_id_get(user_id)

Get user by ID

### Example


```python
import openapi_client
from openapi_client.models.user_response import UserResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://127.0.0.1:5000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user_id = 56 # int | 

    try:
        # Get user by ID
        api_response = api_instance.api_v1_users_user_id_get(user_id)
        print("The response of DefaultApi->api_v1_users_user_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->api_v1_users_user_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User detail |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


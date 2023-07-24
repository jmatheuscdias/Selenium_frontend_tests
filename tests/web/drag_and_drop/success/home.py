from selenium import webdriver
from selenium.webdriver.common.by import By
from seletools.actions import drag_and_drop
import time


def test_drag_n_drop():
    # Defining the webdriver/browser and the initial test URL
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com")
    driver.maximize_window()

    # Validating if it landed on the correct page, here using a native function to check the HTML tag <title> of the page.
    assert driver.title == "The Internet"
    
    # This function will be used to temporarily pause the execution, so the actions can be propperly visualized
    time.sleep(1)

    # Finding the clickable hyperlink to the drag and drop example page, here using xpath, then clicking on it
    goto_drag_n_drop = driver.find_element(By.XPATH, "//a[@href='/drag_and_drop']")
    goto_drag_n_drop.click()

    # Validating if it landed on the correct page, here using the same function as before, but on a header tag <h3>, as the tag <title> hasn't been changed
    example_title = driver.find_element(By.TAG_NAME, "h3")
    assert "Drag and Drop" in example_title.text
    
    time.sleep(1)

    # Mapping the components that will be manipulated. In this case, two divs that share the same class. Thus, a list containing these two items will be defined
    child_divs = driver.find_elements(By.CLASS_NAME, "column")
    
    # Firstly, defining the string value inside the <header> tag from the div at the first position, then confirming we got the right value, which we already know it should be "A" 
    first_child_header = child_divs[0].find_element(By.TAG_NAME, "header")
    print("\nFirst_child header value: " + first_child_header.text)
    assert "A" in first_child_header.text

    # Manipulating the components using a drag and drop action from the 'seletools' library [https://pypi.org/project/seletools], as the tries using native action functions weren't successful
    drag_and_drop(driver, child_divs[0], child_divs[1])
    
    # Defining, after the drag and drop, the content in the <header> tag from the div at the first position, which should be now the value previously owned by the div at the second position, before the drag and drop action was performed. The value obtained now should be "B"
    first_child_header = child_divs[0].find_element(By.TAG_NAME, "header")
    print("New first_child header value: " + first_child_header.text)

    # Asserting if the value is now, in fact, "B"
    assert "B" in first_child_header.text
    
    # Here we have an assertion that should fail this test. To check it, the assertion above can not be executed. You can comment it 
    # assert "A" in first_child_header.text
    
    time.sleep(1)
    
    driver.quit()
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  
    context = browser.new_context()
    page = context.new_page()

    page.goto('http://instagram.com')
    page.set_viewport_size({"width": 1920, "height": 1080})

    page.wait_for_timeout(4000)  
    page.wait_for_timeout(2000)

    # Clicando no elemento
    page.click('xpath=/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')

    # Digitando texto no campo
    page.type('xpath=/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input', 'fabioz')
    page.wait_for_timeout(2000)
    page.click('xpath=/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
    page.wait_for_timeout(2000)
    
    page.type('xpath=/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input', '1111111')
    page.wait_for_timeout(1500)
    page.click('xpath=/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div')
    
    
    page.wait_for_timeout(2000)
    page.wait_for_timeout(2000000)
    browser.close()

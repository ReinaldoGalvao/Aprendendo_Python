from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  
    context = browser.new_context()
    page = context.new_page()

    page.goto('http://instagram.com')
    page.set_viewport_size({"width": 1366, "height": 768})

    page.wait_for_timeout(4000)  
    page.wait_for_timeout(2000)

    # Clicando no elemento
    page.click('xpath=/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')

    # Digitando texto no campo
    page.type('xpath=/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input', 'crovis@mail.com')
    page.wait_for_timeout(2000)
    page.click('xpath=/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
    page.wait_for_timeout(2000)
    
    page.type('xpath=/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input', '796410Qq**')
    page.wait_for_timeout(1500)
    page.click('xpath=/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div')

    page.wait_for_timeout(1357)
    page.click('xpath=/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div')

    page.wait_for_timeout(1557)
    page.click('xpath=/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
    
    #like na primeira publicação
    page.wait_for_timeout(1547)
    page.click('xpath=/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[1]/div/div[2]/div/div[1]/div/article[1]/div/div[3]/div/div/div[1]/div[1]/span[1]/div/div')

    



    
    page.wait_for_timeout(2000)
    page.wait_for_timeout(2000000)
    browser.close()

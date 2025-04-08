@echo off
echo Generating static files with Frozen-Flask...
python freeze.py

echo Setting up gh-pages branch...
:: Check if gh-pages branch exists
git branch | findstr "gh-pages" > nul
if %errorlevel% equ 0 (
    :: If branch exists, switch to it
    git checkout gh-pages
    :: Clear files but preserve .git directory
    for /d %%d in (*) do if not "%%d"==".git" rd /s /q "%%d"
    del /q *
) else (
    :: Create orphan branch with no history
    git checkout --orphan gh-pages
    :: Remove all files from staging
    git rm -rf .
)

echo Copying static files...
:: Copy build files to root
xcopy /E /Y build\* .

:: Create .nojekyll file to prevent GitHub from running Jekyll
echo. > .nojekyll

:: Add all files to git
git add .

:: Commit changes
git commit -m "Update GitHub Pages"

echo Pushing to GitHub...
:: Push to GitHub
git push origin gh-pages

:: Switch back to main branch
git checkout main

echo Deployment complete! Your site should be available at https://YOUR_USERNAME.github.io/python-portfolio/
echo It may take a few minutes for changes to appear.
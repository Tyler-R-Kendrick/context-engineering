#!/bin/bash

echo "🚀 Setting up dev dependencies..."

# Install Node.js development dependencies only
echo "📦 Installing Node.js development dependencies..."
if [ -f "package.json" ]; then
    npm install --only=dev
    echo "✅ Node.js development dependencies installed"

    # Install Playwright browsers
    echo "🌐 Installing Playwright browsers..."
    npx playwright install chromium --with-deps
else
    echo "⚠️  package.json not found, skipping npm install"
fi

# Install Python development dependencies from requirements-dev.txt
echo "📦 Installing Python development dependencies..."
if [ -f "requirements-dev.txt" ]; then
    pip install -r requirements-dev.txt
    echo "✅ Python development dependencies installed from requirements-dev.txt"
else
    echo "⚠️  requirements-dev.txt not found, skipping pip install"
fi

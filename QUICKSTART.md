# Quick Start Guide

Get up and running with Context Engineering materials in 5 minutes!

## 🚀 Choose Your Path

### Path 1: View the Presentation (5 minutes)
Perfect for getting an overview of concepts.

```bash
npm install
npm run dev
```

Open browser to `http://localhost:3030` and navigate through the slides.

---

### Path 2: Interactive Learning (45-60 minutes)
Best for hands-on learners.

**Prerequisites:** 
- VS Code
- Polyglot Notebooks extension
- .NET SDK 8.0+

**Steps:**
1. Open VS Code in this directory
2. Navigate to `notebooks/`
3. Open `01-prompt-engineering-basics.ipynb`
4. Select `.NET Interactive` kernel
5. Run cells and complete exercises

---

### Path 3: Workshop Mode (90-120 minutes)
Ideal for team learning or thorough practice.

**Steps:**
1. Review `workshops/README.md` for overview
2. Complete exercises in order:
   - `exercise-01-improving-prompts.md` (15 min)
   - `exercise-02-context-comments.md` (20 min)
   - `exercise-03-test-driven-context.md` (25 min)
   - `exercise-04-tools-and-context.md` (30 min)
3. Apply learnings to real code

---

### Path 4: Reference Mode (As needed)
Use templates and patterns in your daily work.

**Quick Access:**
- **Prompty Templates:** See `prompty/README.md`
- **Pattern Examples:** See notebooks
- **Workshop Exercises:** See workshops directory

---

## 📦 Installation

### Minimal Setup (Presentation Only)
```bash
npm install
```

### Full Setup (All Features)
```bash
# 1. Install Node.js dependencies
npm install

# 2. Install VS Code extensions
code --install-extension ms-dotnettools.dotnet-interactive-vscode

# 3. Install .NET SDK 8.0+ from dotnet.microsoft.com
# Verify installation:
dotnet --version
```

---

## 🎯 First Steps by Role

### Individual Developer
1. ✅ Watch presentation (30 min)
2. ✅ Try first notebook (30 min)
3. ✅ Apply one technique today
4. ✅ Share results with team

### Team Lead
1. ✅ Review all materials (60 min)
2. ✅ Schedule team workshop
3. ✅ Customize templates for team
4. ✅ Establish team standards

### Student/Learner
1. ✅ Complete presentation
2. ✅ Work through all notebooks
3. ✅ Complete all workshops
4. ✅ Create your own examples

---

## 🔑 Key Files

| File | Purpose | Time |
|------|---------|------|
| `slides.md` | Main presentation | 45-60 min |
| `notebooks/01-*.ipynb` | Basic concepts | 30 min |
| `notebooks/02-*.ipynb` | Advanced patterns | 45 min |
| `workshops/exercise-01-*.md` | Prompt improvement | 15 min |
| `workshops/exercise-02-*.md` | Context comments | 20 min |
| `workshops/exercise-03-*.md` | Test-driven | 25 min |
| `workshops/exercise-04-*.md` | Tools integration | 30 min |
| `prompty/*.prompty` | Reusable templates | Reference |

---

## ⚡ Quick Commands

```bash
# Start presentation
npm run dev

# Build static site
npm run build

# Export as PDF
npm run export

# View what's included
ls -R notebooks/ prompty/ workshops/
```

---

## 🆘 Troubleshooting

### Presentation won't start?
```bash
# Clear cache and reinstall
rm -rf node_modules package-lock.json
npm install
npm run dev
```

### Notebooks won't open?
1. Install Polyglot Notebooks extension in VS Code
2. Install .NET SDK 8.0+
3. Restart VS Code
4. Open `.ipynb` file
5. Select `.NET Interactive` kernel

### Missing dependencies?
```bash
# Check Node.js
node --version  # Should be 18+

# Check .NET
dotnet --version  # Should be 8.0+

# Check npm
npm --version
```

---

## 📚 Learning Checklist

Use this to track your progress:

### Week 1: Fundamentals
- [ ] Watch presentation slides 1-25
- [ ] Complete notebook 1
- [ ] Do workshop exercise 1
- [ ] Apply to one real task

### Week 2: Application
- [ ] Watch presentation slides 26-50
- [ ] Complete notebook 2
- [ ] Do workshop exercises 2-3
- [ ] Create team template

### Week 3: Mastery
- [ ] Complete workshop exercise 4
- [ ] Customize prompty templates
- [ ] Share with team
- [ ] Measure improvements

---

## 🎓 Certification

After completing all materials, you should be able to:

✅ Write specific, effective prompts
✅ Provide proper context through multiple methods
✅ Use tests to drive implementation
✅ Leverage tools for better results
✅ Apply patterns to real-world scenarios
✅ Teach others these techniques

---

## 🤝 Next Steps

1. **Choose your path** above
2. **Start learning** today
3. **Apply immediately** to your work
4. **Share results** with your team
5. **Iterate and improve** your techniques

---

## 💡 Pro Tips

- 🎯 **Start Small:** Pick one technique and use it today
- 🔄 **Iterate:** Refine your prompts based on results
- 📝 **Document:** Keep notes on what works
- 👥 **Share:** Teach teammates what you learn
- 🚀 **Practice:** Daily application builds expertise

---

## 📞 Need Help?

- 📖 Check directory READMEs for detailed info
- 🐛 Open an issue for bugs
- 💬 Start a discussion for questions
- 🤝 Contribute improvements via PR

---

**Ready?** Pick a path above and start your context engineering journey! 🚀

---
Modified: 2025-02-19T17:10:19-06:00
title: Integrating ProGet with Chocolatey
tags:
  - chocolatey
---
If you want to use **ProGet as a private Chocolatey repository**, follow these steps to **host, push, and install Chocolatey packages** from ProGet.

---

## **1. Create a Chocolatey Feed in ProGet**

1. **Log into your ProGet Web UI** (`http://localhost:81` or your configured address).
2. **Go to** `Feeds` → `Create New Feed`.
3. **Select Feed Type:** `Chocolatey`.
4. **Give it a name**, e.g., `choco-packages`.
5. **Configure permissions** (optional) to control who can push/install packages.
6. **Click "Create Feed"**.

---

## **2. Configure Chocolatey to Use ProGet**

Run this in **PowerShell** (as Admin) to add ProGet as a Chocolatey source:

```powershell
choco source add -n="ProGetChoco" -s "http://proget.local/chocolatey/choco-packages/"
```

> Replace `proget.local` with your **actual ProGet server URL**.

Verify the source was added:

```powershell
choco source list
```

---

## **3. Upload or Push Chocolatey Packages**

### **A. Manually Upload Packages**

1. Download a `.nupkg` Chocolatey package from `https://community.chocolatey.org/`.
2. Go to your ProGet feed (`http://proget.local/chocolatey/choco-packages/`).
3. Click **Upload Package** → Select the `.nupkg` file.
4. Click **Upload**.

### **B. Push Packages Using API Key**

1. Generate an API key in ProGet:
    - Go to `User Profile` → `API Keys` → `Create API Key`.
2. Use this PowerShell command to push a package:

```powershell
choco push mypackage.nupkg --source http://proget.local/chocolatey/choco-packages/ --api-key YOUR_API_KEY
```

---

## **4. Install Chocolatey Packages from ProGet**

Now that your packages are hosted in ProGet, install them like this:

```powershell
choco install mypackage -s "http://proget.local/chocolatey/choco-packages/"
```

To make ProGet the **default Chocolatey source**, remove the default Chocolatey community source:

```powershell
choco source remove -n="chocolatey"
```

---

## **5. Automate & Secure**

- **Enable SSL (HTTPS)** in IIS for security.
- **Restrict Access** by requiring authentication for Chocolatey package downloads.
- **Use Retention Policies** to clean up old package versions.

---

Now you have a **private Chocolatey repository** using ProGet! 🎉
# Multi-Format Output Support

## Overview
The Design System Agent now supports generating components in **3 formats**:
- **React/JSX** - React components (default)
- **HTML** - Pure HTML markup
- **JSON** - Structured component specifications

## API Usage

### 1. Generate React Component (Default)
```json
POST /api/v1/query
{
  "query": "create a login page",
  "format": "react"
}
```

**Response:**
```javascript
import { Card, Input, Button } from '@/components';

function LoginPage() {
  return (
    <div className="flex justify-center">
      <Card>
        <Input type="email" label="Email" />
        <Button variant="primary">Sign In</Button>
      </Card>
    </div>
  );
}
```

### 2. Generate HTML
```json
POST /api/v1/query
{
  "query": "create a login page",
  "format": "html"
}
```

**Response:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Login</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="auth-container">
        <div class="card">
            <form class="auth-form">
                <input type="email" placeholder="Enter your email" required />
                <input type="password" placeholder="Enter your password" required />
                <button type="submit" class="btn btn-primary">Sign In</button>
            </form>
        </div>
    </div>
</body>
</html>
```

### 3. Generate JSON Specification
```json
POST /api/v1/query
{
  "query": "create a login page",
  "format": "json"
}
```

**Response:**
```json
{
  "type": "page",
  "template": "auth",
  "title": "Login",
  "layout": {
    "type": "centered",
    "maxWidth": "md"
  },
  "components": [
    {
      "type": "card",
      "content": {
        "type": "form",
        "fields": [
          {
            "name": "email",
            "type": "email",
            "label": "Email",
            "required": true
          },
          {
            "name": "password",
            "type": "password",
            "label": "Password",
            "required": true
          }
        ]
      }
    }
  ]
}
```

## Examples

### Dashboard

**React:**
```json
{"query": "build analytics dashboard", "format": "react"}
```
Returns JSX with Grid, Card components

**HTML:**
```json
{"query": "build analytics dashboard", "format": "html"}
```
Returns complete HTML page with dashboard-grid

**JSON:**
```json
{"query": "build analytics dashboard", "format": "json"}
```
Returns structured spec:
```json
{
  "type": "dashboard",
  "widgets": [
    {"type": "stat-card", "title": "Total Users", "value": "1,234"},
    {"type": "chart-card", "chartType": "line"}
  ]
}
```

### Button Component

**React:**
```json
{"query": "primary button", "format": "react"}
```
→ `<Button variant="primary">Click me</Button>`

**HTML:**
```json
{"query": "primary button", "format": "html"}
```
→ `<button class="btn btn-primary">Click me</button>`

**JSON:**
```json
{"query": "primary button", "format": "json"}
```
→ `{"type": "button", "variant": "primary", "text": "Click me"}`

## Use Cases

### HTML Format
- **Static websites**
- **Email templates**
- **Server-side rendering**
- **SEO-friendly pages**
- **Plain HTML prototypes**

### JSON Format
- **API contracts**
- **Component libraries**
- **Design tokens**
- **CMS integration**
- **Low-code platforms** (like Lovable, Bubble)
- **Mobile apps** (React Native, Flutter)
- **Cross-platform** rendering

### React Format
- **React applications**
- **Next.js projects**
- **Component libraries**
- **Storybook documentation**

## Format Detection

The system automatically detects the correct syntax highlighting:
- `react` → `jsx`
- `html` → `html`
- `json` → `json`

## Testing

```bash
# Start server
uvicorn design_system_agent.api.main:app --reload

# Test HTML
curl -X POST http://localhost:8000/api/v1/query \
  -H "Content-Type: application/json" \
  -d '{"query": "create a button", "format": "html"}'

# Test JSON
curl -X POST http://localhost:8000/api/v1/query \
  -H "Content-Type: application/json" \
  -d '{"query": "create a dashboard", "format": "json"}'

# Test React (default)
curl -X POST http://localhost:8000/api/v1/query \
  -H "Content-Type: application/json" \
  -d '{"query": "create a login page"}'
```

## Benefits

✅ **Flexibility**: Choose output based on your stack  
✅ **Interoperability**: JSON works with any framework  
✅ **Simplicity**: HTML for static sites  
✅ **Modern**: React for SPAs  
✅ **Universal**: JSON specs can be consumed anywhere  

Perfect for building tools like **Lovable.dev**, **v0.dev**, or **Google AI Studio**! 🎉

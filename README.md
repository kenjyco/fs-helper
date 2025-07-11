A collection of essential filesystem and logging utilities designed to eliminate daily friction in Python development. `fs-helper` provides production-grade implementations of fundamental operations that developers need constantly but often implement inconsistently across projects.

This library embodies a philosophy of **invisible infrastructure** becoming so reliable and predictable that you forget you're using it. Every function is designed to solve a problem completely on first invocation, with zero-configuration defaults that work in production immediately while providing comprehensive control when needed.

**Who benefits from this:**
- **DevOps engineers** automating deployment and monitoring workflows
- **Python developers** building command-line tools and scripts
- **Data scientists** managing file-based workflows and logging
- **Anyone** tired of reimplementing the same filesystem and logging patterns across projects

**How it fits into your toolchain:**
`fs-helper` serves as foundational infrastructure that other tools can depend on. It's designed to compose naturally with shell scripts, provide REPL-friendly exploration, and integrate seamlessly into existing Python projects without imposing architectural constraints.

## Install

```
pip install fs-helper
```

## QuickStart

```python
import fs_helper as fh

# Production-ready logging in one line
logger = fh.get_logger(__name__)
logger.info("Application started")

# Safe path handling that works everywhere
log_dir = fh.abspath("~/logs")

# Convert any text to a safe filename
safe_name = fh.lazy_filename("User Data: Report (2024)")
# Returns: "User-Data--Report-2024"

# Git-aware path resolution
repo_root = fh.repopath()  # Returns None if not in a git repo
if repo_root:
    print(f"Working in repository: {repo_root}")

# File monitoring for automation workflows
fh.wait_for_write_age("output.log", age=5, verbose=True)
print("Log file has been stable for 5 seconds, proceeding...")
```

**What you gain:** Immediate access to bulletproof implementations of common operations with comprehensive error handling, cross-platform compatibility, and zero configuration overhead. Functions gracefully handle edge cases (missing directories, permission issues, invalid paths) so your code can focus on domain logic rather than infrastructure concerns.

## API Overview

### Core Path Operations

- **`abspath(filepath)`** - Enhanced path normalization with tilde expansion
  - `filepath`: Path string to normalize
  - Returns: Absolute path as string
  - Internal calls: None

- **`strip_extension(filepath)`** - Remove file extension from path
  - `filepath`: Path string
  - Returns: Path without extension
  - Internal calls: None

- **`get_extension(filepath)`** - Extract file extension from path
  - `filepath`: Path string
  - Returns: Extension without leading dot
  - Internal calls: None

- **`repopath(filepath='')`** - Find git repository root for given path
  - `filepath`: Path to check (defaults to current directory)
  - Returns: Repository root path or `None` if not in a git repo
  - Internal calls: `abspath()`

### Production Logging

- **`get_logger(module_name, logdir=DEFAULT_LOG_DIR, file_format='%(asctime)s - %(levelname)s - %(funcName)s: %(message)s', stream_format='%(asctime)s: %(message)s', file_level=logging.DEBUG, stream_level=logging.INFO)`** - Create production-ready logger with file and console output
  - `module_name`: Logger identifier (typically `__name__`)
  - `logdir`: Directory for log files (defaults to `~/logs`, falls back to `/tmp/logs`)
  - `file_format`: Log format for file output (set to empty string to disable)
  - `stream_format`: Log format for console output (set to empty string to disable)
  - `file_level`: Logging level for file (accepts strings like 'info' or integers)
  - `stream_level`: Logging level for console
  - Returns: Configured logger instance with automatic directory creation and fallback strategies
  - Internal calls: `abspath()`

- **`get_logfile_from_logger(logger)`** - Extract log file path from logger instance
  - `logger`: Logger object
  - Returns: Path to log file or `None` if no file handler
  - Internal calls: None

- **`get_logger_filenames(logger)`** - Get all log file paths from logger
  - `logger`: Logger object
  - Returns: List of log file paths
  - Internal calls: None

### File Utilities

- **`lazy_filename(text, ext='')`** - Convert arbitrary text to safe filenames
  - `text`: Input text to convert (URLs, user input, API responses)
  - `ext`: Optional extension to append
  - Returns: Safe filename string with unsafe characters removed
  - Internal calls: None

- **`sha256sum(filepath)`** - Calculate SHA256 checksum of file
  - `filepath`: Path to file
  - Returns: Hexadecimal SHA256 digest
  - Internal calls: `abspath()`

### Package Analysis

- **`get_local_package_info(dirpath, exception=True)`** - Extract packaging information from Python project directory
  - `dirpath`: Path to project directory
  - `exception`: If True, raise exception for non-Python projects
  - Returns: Dictionary with keys: `setup.py_path`, `setup.py_content`, `pyproject.toml_path`, `pyproject.toml_content`
  - Internal calls: `abspath()`

### Monitoring and Coordination

- **`wait_for_write_age(filepath, age=10, sleeptime=1, verbose=False)`** - Wait until file hasn't been modified for specified duration
  - `filepath`: File to monitor
  - `age`: Seconds since last write required
  - `sleeptime`: Polling interval in seconds
  - `verbose`: If True, print status messages
  - Returns: `True` when condition met
  - Internal calls: `abspath()`

- **`wait_for_empty_directory(dirpath, sleeptime=1, verbose=False)`** - Wait until directory contains no files
  - `dirpath`: Directory to monitor
  - `sleeptime`: Polling interval in seconds
  - `verbose`: If True, print status messages
  - Returns: `True` when directory is empty
  - Internal calls: `abspath()`

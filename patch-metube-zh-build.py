from pathlib import Path
import glob

root = Path('/app/ui/dist/metube/browser')

main_files = list(root.glob('main-*.js'))
if not main_files:
    print('No main JS file found')
    exit(1)
main = main_files[0]
s = main.read_text(encoding='utf-8')

strings = {
    'Light': '浅色',
    'Dark': '深色',
    'Auto': '自动',
    'Video': '视频',
    'Audio': '音频',
    'Captions': '字幕',
    'Thumbnail': '缩略图',
    'Best': '最佳',
    'Worst': '最差',
    'iOS Compatible': '兼容 iOS',
    'Auto Only': '仅自动',
    'Manual Only': '仅手动',
    'Prefer Auto': '优先自动',
    'Prefer Manual': '优先手动',
    'TXT (Text only)': 'TXT（仅文本）',
    'Newest first': '最新优先',
    'Oldest first': '最旧优先',
    'Advanced Options': '高级选项',
    'Output': '输出',
    'Behavior': '行为',
    'Tools': '工具',
    'Cookies': 'Cookie',
    'Import URLs': '导入链接',
    'Export URLs': '导出链接',
    'Copy URLs': '复制链接',
    'Close': '关闭',
    'Downloading': '下载中',
    'Completed': '已完成',
    'Subscriptions': '订阅',
    'Speed': '速度',
    'Type': '类型',
    'Quality': '质量',
    'Downloaded': '已下载',
    'Name': '名称',
    'Filter': '过滤器',
    'Status': '状态',
    'Yes': '是',
    'No': '否',
    'URL': '链接',
    'ETA': '剩余时间',
    'Codec / Format': '编码 / 格式',
    'Add a prefix to downloaded filenames.': '为下载文件名添加前缀。',
    'Auto Start': '自动开始',
    'Automatically start downloads when added.': '添加后自动开始下载。',
    'Batch Import URLs': '批量导入链接',
    'Bulk Actions': '批量操作',
    'Cancel adding URL': '取消添加链接',
    'Check all now': '立即检查全部',
    'Check now': '立即检查',
    'Check selected': '检查所选',
    'Checking': '检查中',
    'Checking now': '正在检查',
    'Choose manual, auto, or fallback preference for captions mode.': '选择字幕模式：手动、自动或优先策略。',
    'Choose one or more yt-dlp option presets configured on the server (applied in order).': '选择一个或多个服务器配置的 yt-dlp 选项预设（按顺序应用）。',
    'Click for details': '点击查看详情',
    'Clip end': '片段结束',
    'Clip start': '片段开始',
    'Copied!': '已复制！',
    'Copy error details to clipboard': '复制错误详情到剪贴板',
    'Custom Name Prefix': '自定义文件名前缀',
    'Custom yt-dlp Options': '自定义 yt-dlp 选项',
    'Custom yt-dlp options must be a JSON object': '自定义 yt-dlp 选项必须是 JSON 对象',
    'Custom yt-dlp options must be valid JSON': '自定义 yt-dlp 选项必须是有效 JSON',
    'Delete completed item': '删除已完成项目',
    'Delete subscription': '删除订阅',
    'Delete subscription failed': '删除订阅失败',
    'Delete subscriptions failed': '删除订阅失败',
    'Download Folder': '下载文件夹',
    'Download chapter file': '下载章节文件',
    'Download or subscribe': '下载或订阅',
    'Download result file for': '下载结果文件：',
    'Edit subscription title filter (subscriptions only; not for one-off downloads)': '编辑订阅标题过滤器（仅订阅，不影响单次下载）',
    'Enter video, channel, or playlist URL': '输入视频、频道或播放列表链接',
    'Error deleting cookies.': '删除 Cookie 出错。',
    'Error reloading yt-dlp options:': '重新加载 yt-dlp 选项出错：',
    'Error uploading cookies.': '上传 Cookie 出错。',
    'Failed to cancel adding:': '取消添加失败：',
    'Failed to copy URLs.': '复制链接失败。',
    'Failed to copy to clipboard. Your browser may require HTTPS for clipboard access.': '复制到剪贴板失败。浏览器可能要求 HTTPS 才能访问剪贴板。',
    'File Size': '文件大小',
    'How often to poll subscriptions for new videos.': '检查订阅新视频的间隔。',
    'Interval (min)': '间隔（分钟）',
    'Invalid subscription title filter (regex)': '订阅标题过滤器无效（正则表达式）',
    'Items Limit': '项目数量限制',
    'Last checked': '上次检查',
    'Maximum number of items to download from a playlist or channel (0 = no limit).': '播放列表或频道最多下载项目数（0 表示无限制）。',
    'MeTube Logo': 'MeTube 标志',
    'No URLs found for the selected filter.': '所选筛选条件下没有找到链接。',
    'No results available': '没有可用结果',
    'Open chapter file': '打开章节文件',
    'Open source URL for': '打开源链接：',
    'Option Presets': '选项预设',
    'Optional end time. Blank = until end of media.': '可选结束时间。留空表示直到媒体结束。',
    'Optional per-download yt-dlp overrides as a JSON object.': '可选：为本次下载单独设置 yt-dlp JSON 参数。',
    'Optional regex': '可选正则表达式',
    'Optional start time (seconds, M:SS, or H:MM:SS). Blank = from start or YouTube &t= in URL.': '可选开始时间（秒、M:SS 或 H:MM:SS）。留空表示从开头或使用 YouTube 链接里的 &t=。',
    'Output template for chapter files.': '章节文件的输出模板。',
    'Paste one video URL per line': '每行粘贴一个视频链接',
    'Pause': '暂停',
    'Please enter a URL': '请输入链接',
    'Refresh subscriptions failed': '刷新订阅失败',
    'Remove': '移除',
    'Remove uploaded cookies': '移除已上传 Cookie',
    'Replace Cookies': '替换 Cookie',
    'Request failed': '请求失败',
    'Resume': '继续',
    'Retry download for': '重试下载：',
    'Select all subscriptions': '选择所有订阅',
    'Select all': '全选',
    'Select item': '选择项目',
    'Select subscription': '选择订阅',
    'Share result file for': '分享结果文件：',
    'Skip members-only subscription videos': '跳过会员专属订阅视频',
    'Split by chapters': '按章节拆分',
    'Start download for': '开始下载：',
    'Subscribe failed': '订阅失败',
    'Subscription Check (min)': '订阅检查（分钟）',
    'Subscription Title Filter': '订阅标题过滤器',
    'Subscription check failed': '订阅检查失败',
    'Subscriptions only — which new video titles to queue when this feed is checked. Does not affect manual downloads.': '仅订阅使用：检查该订阅源时，哪些新视频标题会加入队列。不影响手动下载。',
    'Subtitle Source': '字幕来源',
    'Subtitle language (you can type any language code).': '字幕语言（可输入任意语言代码）。',
    'Subtitle output format for captions mode.': '字幕模式的字幕输出格式。',
    'Type to filter existing folders, or enter a new folder name.': '输入以筛选已有文件夹，或输入新文件夹名称。',
    'URLs copied to clipboard.': '链接已复制到剪贴板。',
    'Unknown Error': '未知错误',
    'Unknown error': '未知错误',
    'Update subscription failed': '更新订阅失败',
    'Upload Cookies': '上传 Cookie',
    'Upload a cookies.txt file from your browser to authenticate restricted or private downloads.': '上传浏览器导出的 cookies.txt 文件，用于访问受限或私有下载。',
}

for old, new in strings.items():
    for quote in ['"', "'"]:
        s = s.replace(f'{quote}{old}{quote}', f'{quote}{new}{quote}')

main.write_text(s, encoding='utf-8')

index = root / 'index.html'
html = index.read_text(encoding='utf-8')
html = html.replace('<html lang="en"', '<html lang="zh-CN"')
html = html.replace('<title>MeTube</title>', '<title>MeTube 视频下载</title>')
html = html.replace('Please enable JavaScript to continue using this application.', '请启用 JavaScript 以继续使用此应用。')

old_main_name = main.name
new_main = root / f'{main.stem}-zh{main.suffix}'
if new_main.exists():
    new_main.unlink()
main.rename(new_main)
html = html.replace(old_main_name, new_main.name)
index.write_text(html, encoding='utf-8')

manifest = root / 'manifest.webmanifest'
if manifest.exists():
    m = manifest.read_text(encoding='utf-8')
    m = m.replace('"name": "MeTube"', '"name": "MeTube 视频下载"')
    manifest.write_text(m, encoding='utf-8')

print(f'Patched: {new_main.name}')
print(f'Replacements: {len(strings)}')

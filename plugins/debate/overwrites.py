from discord import PermissionOverwrite


# Base Permissions
BASE: PermissionOverwrite = PermissionOverwrite()

# All Safe Permissions
GLOBAL_SAFE: PermissionOverwrite = PermissionOverwrite(
    create_instant_invite=False,
    manage_channels=True,
    add_reactions=True,
    priority_speaker=True,
    stream=True,
    view_channel=True,
    send_messages=True,
    send_tts_messages=False,
    manage_messages=True,
    embed_links=True,
    attach_files=True,
    read_message_history=True,
    mention_everyone=True,
    external_emojis=True,
    connect=True,
    speak=True,
    mute_members=True,
    deafen_members=True,
    move_members=True,
    use_voice_activation=True,
    manage_permissions=True,
    manage_webhooks=False,
    manage_threads=True,
    use_threads=True,
    use_private_threads=True,
)

# Director Level
DIRECTOR_BASE: PermissionOverwrite = PermissionOverwrite(
    create_instant_invite=True,
    manage_channels=False,
    add_reactions=True,
    priority_speaker=True,
    stream=True,
    view_channel=True,
    send_messages=True,
    send_tts_messages=False,
    manage_messages=True,
    embed_links=True,
    attach_files=True,
    read_message_history=True,
    mention_everyone=True,
    external_emojis=True,
    connect=True,
    speak=True,
    mute_members=True,
    deafen_members=True,
    move_members=True,
    use_voice_activation=True,
    manage_permissions=False,
    manage_webhooks=False,
    manage_threads=True,
    use_threads=True,
    use_private_threads=True,
)

DIRECTOR_READ_ONLY: PermissionOverwrite = PermissionOverwrite(
    create_instant_invite=True,
    manage_channels=False,
    add_reactions=False,
    priority_speaker=False,
    stream=False,
    view_channel=True,
    send_messages=False,
    send_tts_messages=False,
    manage_messages=False,
    embed_links=True,
    attach_files=True,
    read_message_history=True,
    mention_everyone=False,
    external_emojis=False,
    connect=False,
    speak=False,
    mute_members=False,
    deafen_members=False,
    move_members=False,
    use_voice_activation=False,
    manage_permissions=False,
    manage_webhooks=False,
    manage_threads=False,
    use_threads=False,
    use_private_threads=False,
)

DIRECTOR_MODERATION: PermissionOverwrite = PermissionOverwrite(
    create_instant_invite=False,
    manage_channels=False,
    add_reactions=True,
    priority_speaker=False,
    stream=True,
    view_channel=True,
    send_messages=True,
    send_tts_messages=False,
    manage_messages=False,
    embed_links=True,
    attach_files=True,
    read_message_history=True,
    mention_everyone=True,
    external_emojis=True,
    connect=True,
    speak=True,
    mute_members=True,
    deafen_members=True,
    move_members=True,
    use_voice_activation=True,
    manage_permissions=False,
    manage_webhooks=False,
    manage_threads=False,
    use_threads=True,
    use_private_threads=True,
)

DIRECTOR_LOGS: PermissionOverwrite = PermissionOverwrite(
    create_instant_invite=False,
    manage_channels=False,
    add_reactions=False,
    priority_speaker=False,
    stream=False,
    view_channel=True,
    send_messages=False,
    send_tts_messages=False,
    manage_messages=False,
    embed_links=True,
    attach_files=True,
    read_message_history=True,
    mention_everyone=False,
    external_emojis=False,
    connect=False,
    speak=False,
    mute_members=False,
    deafen_members=False,
    move_members=False,
    use_voice_activation=False,
    manage_permissions=False,
    manage_webhooks=False,
    manage_threads=False,
    use_threads=False,
    use_private_threads=False,
)

# Moderator Level
MODERATOR_BASE: PermissionOverwrite = PermissionOverwrite(
    create_instant_invite=True,
    manage_channels=False,
    add_reactions=True,
    priority_speaker=True,
    stream=True,
    send_messages=True,
    send_tts_messages=False,
    manage_messages=True,
    embed_links=True,
    attach_files=True,
    read_message_history=True,
    mention_everyone=False,
    external_emojis=True,
    connect=True,
    speak=True,
    mute_members=True,
    deafen_members=True,
    move_members=True,
    use_voice_activation=True,
    manage_permissions=False,
    manage_webhooks=False,
    manage_threads=True,
    use_threads=True,
    use_private_threads=True,
)

MODERATOR_MODERATION: PermissionOverwrite = PermissionOverwrite(
    create_instant_invite=False,
    manage_channels=False,
    add_reactions=True,
    priority_speaker=True,
    stream=True,
    view_channel=True,
    send_messages=True,
    send_tts_messages=False,
    manage_messages=False,
    embed_links=True,
    attach_files=True,
    read_message_history=True,
    mention_everyone=False,
    external_emojis=True,
    connect=True,
    speak=True,
    mute_members=False,
    deafen_members=False,
    move_members=False,
    use_voice_activation=True,
    manage_permissions=False,
    manage_webhooks=False,
    manage_threads=False,
    use_threads=True,
    use_private_threads=True,
)

# Citizen Level
CITIZEN_REACT_ONLY: PermissionOverwrite = PermissionOverwrite(
    create_instant_invite=False,
    manage_channels=False,
    add_reactions=True,
    priority_speaker=False,
    stream=False,
    view_channel=None,
    send_messages=False,
    send_tts_messages=False,
    manage_messages=False,
    embed_links=False,
    attach_files=False,
    read_message_history=True,
    mention_everyone=False,
    external_emojis=True,
    connect=False,
    speak=False,
    mute_members=False,
    deafen_members=False,
    move_members=False,
    use_voice_activation=False,
    manage_permissions=False,
    manage_webhooks=False,
    manage_threads=False,
    use_threads=False,
    use_private_threads=False,
)

# Everyone Level
EVERYONE_READ_ONLY: PermissionOverwrite = PermissionOverwrite(
    manage_channels=False,
    add_reactions=False,
    priority_speaker=False,
    stream=False,
    view_channel=None,
    send_messages=False,
    send_tts_messages=False,
    manage_messages=False,
    embed_links=False,
    attach_files=False,
    read_message_history=True,
    mention_everyone=False,
    external_emojis=False,
    connect=False,
    speak=False,
    mute_members=False,
    deafen_members=False,
    move_members=False,
    use_voice_activation=False,
    manage_permissions=False,
    manage_webhooks=False,
    manage_threads=False,
    use_threads=False,
    use_private_threads=False,
)

EVERYONE_EXPLICIT_READ_ONLY: PermissionOverwrite = PermissionOverwrite(
    view_channel=True,
    manage_channels=False,
    add_reactions=False,
    priority_speaker=False,
    stream=False,
    send_messages=False,
    send_tts_messages=False,
    manage_messages=False,
    embed_links=False,
    attach_files=False,
    read_message_history=True,
    mention_everyone=False,
    external_emojis=False,
    connect=False,
    speak=False,
    mute_members=False,
    deafen_members=False,
    move_members=False,
    use_voice_activation=False,
    manage_permissions=False,
    manage_webhooks=False,
    manage_threads=False,
    use_threads=False,
    use_private_threads=False,
)

EVERYONE_SEND_ONLY: PermissionOverwrite = PermissionOverwrite(
    read_messages=True, view_channel=True
)

EVERYONE_NEGATIVE: PermissionOverwrite = PermissionOverwrite(
    create_instant_invite=False,
    manage_channels=False,
    add_reactions=False,
    priority_speaker=False,
    stream=False,
    view_channel=False,
    send_messages=False,
    send_tts_messages=False,
    manage_messages=False,
    embed_links=False,
    attach_files=False,
    read_message_history=False,
    mention_everyone=False,
    external_emojis=False,
    connect=False,
    speak=False,
    mute_members=False,
    deafen_members=False,
    move_members=False,
    use_voice_activation=False,
    manage_permissions=False,
    manage_webhooks=False,
    manage_threads=False,
    use_threads=False,
    use_private_threads=False,
)

EVERYONE_NO_READ: PermissionOverwrite = PermissionOverwrite(view_channel=False)


UNLOCKED_OVERWRITE_MAP = {
    "information": {
        "role_warden": GLOBAL_SAFE,
        "role_director": DIRECTOR_BASE,
        "role_moderator": EVERYONE_READ_ONLY,
        "role_citizen": EVERYONE_READ_ONLY,
        "role_member": EVERYONE_READ_ONLY,
        "role_logs": BASE,
        "role_detained": EVERYONE_NEGATIVE,
        "role_muted": EVERYONE_READ_ONLY,
        "role_super_muted": EVERYONE_NEGATIVE,
        "role_everyone": BASE,
    },
    "verification": {
        "role_warden": GLOBAL_SAFE,
        "role_director": DIRECTOR_BASE,
        "role_moderator": EVERYONE_NEGATIVE,
        "role_citizen": EVERYONE_NEGATIVE,
        "role_member": EVERYONE_NEGATIVE,
        "role_logs": BASE,
        "role_detained": EVERYONE_NEGATIVE,
        "role_muted": EVERYONE_NEGATIVE,
        "role_super_muted": EVERYONE_NEGATIVE,
        "role_everyone": EVERYONE_SEND_ONLY,
    },
    "community_updates": {
        "role_warden": GLOBAL_SAFE,
        "role_director": DIRECTOR_READ_ONLY,
        "role_moderator": EVERYONE_NEGATIVE,
        "role_citizen": EVERYONE_NEGATIVE,
        "role_member": EVERYONE_NEGATIVE,
        "role_logs": BASE,
        "role_detained": EVERYONE_NEGATIVE,
        "role_muted": EVERYONE_NEGATIVE,
        "role_super_muted": EVERYONE_NEGATIVE,
        "role_everyone": EVERYONE_NEGATIVE,
    },
    "moderation": {
        "role_warden": GLOBAL_SAFE,
        "role_director": DIRECTOR_MODERATION,
        "role_moderator": MODERATOR_MODERATION,
        "role_citizen": EVERYONE_NEGATIVE,
        "role_member": EVERYONE_NEGATIVE,
        "role_logs": BASE,
        "role_detained": EVERYONE_NEGATIVE,
        "role_muted": EVERYONE_NEGATIVE,
        "role_super_muted": EVERYONE_NEGATIVE,
        "role_everyone": EVERYONE_NEGATIVE,
    },
    "director_commands": {
        "role_warden": GLOBAL_SAFE,
        "role_director": DIRECTOR_MODERATION,
        "role_moderator": EVERYONE_NEGATIVE,
        "role_citizen": EVERYONE_NEGATIVE,
        "role_member": EVERYONE_NEGATIVE,
        "role_logs": BASE,
        "role_detained": EVERYONE_NEGATIVE,
        "role_muted": EVERYONE_NEGATIVE,
        "role_super_muted": EVERYONE_NEGATIVE,
        "role_everyone": EVERYONE_NEGATIVE,
    },
    "isolation": {
        "role_warden": GLOBAL_SAFE,
        "role_director": EVERYONE_READ_ONLY,
        "role_moderator": EVERYONE_READ_ONLY,
        "role_citizen": EVERYONE_NEGATIVE,
        "role_member": EVERYONE_NEGATIVE,
        "role_logs": BASE,
        "role_detained": EVERYONE_EXPLICIT_READ_ONLY,
        "role_muted": EVERYONE_NEGATIVE,
        "role_super_muted": EVERYONE_NEGATIVE,
        "role_everyone": EVERYONE_NEGATIVE,
    },
    "interface": {
        "role_warden": GLOBAL_SAFE,
        "role_director": DIRECTOR_READ_ONLY,
        "role_moderator": EVERYONE_READ_ONLY,
        "role_citizen": CITIZEN_REACT_ONLY,
        "role_member": EVERYONE_READ_ONLY,
        "role_logs": BASE,
        "role_detained": EVERYONE_NEGATIVE,
        "role_muted": EVERYONE_READ_ONLY,
        "role_super_muted": EVERYONE_NEGATIVE,
        "role_everyone": BASE,
    },
    "commands": {
        "role_warden": GLOBAL_SAFE,
        "role_director": DIRECTOR_BASE,
        "role_moderator": MODERATOR_BASE,
        "role_citizen": BASE,
        "role_member": BASE,
        "role_logs": BASE,
        "role_detained": EVERYONE_NEGATIVE,
        "role_muted": EVERYONE_READ_ONLY,
        "role_super_muted": EVERYONE_NEGATIVE,
        "role_everyone": BASE,
    },
    "community": {
        "role_warden": GLOBAL_SAFE,
        "role_director": DIRECTOR_BASE,
        "role_moderator": MODERATOR_BASE,
        "role_citizen": BASE,
        "role_member": BASE,
        "role_logs": BASE,
        "role_detained": EVERYONE_NEGATIVE,
        "role_muted": EVERYONE_READ_ONLY,
        "role_super_muted": EVERYONE_NEGATIVE,
        "role_everyone": BASE,
    },
    "debate": {
        "role_warden": GLOBAL_SAFE,
        "role_director": DIRECTOR_BASE,
        "role_moderator": MODERATOR_BASE,
        "role_citizen": BASE,
        "role_member": BASE,
        "role_logs": BASE,
        "role_detained": EVERYONE_NEGATIVE,
        "role_muted": EVERYONE_READ_ONLY,
        "role_super_muted": EVERYONE_NEGATIVE,
        "role_everyone": BASE,
    },
    "debate-#": {
        "role_warden": GLOBAL_SAFE,
        "role_director": DIRECTOR_BASE,
        "role_moderator": MODERATOR_BASE,
        "role_citizen": EVERYONE_NO_READ,
        "role_member": EVERYONE_NO_READ,
        "role_logs": BASE,
        "role_detained": EVERYONE_NEGATIVE,
        "role_muted": EVERYONE_NEGATIVE,
        "role_super_muted": EVERYONE_NEGATIVE,
        "role_everyone": BASE,
    },
    "logs": {
        "role_warden": GLOBAL_SAFE,
        "role_director": DIRECTOR_LOGS,
        "role_moderator": EVERYONE_NEGATIVE,
        "role_citizen": EVERYONE_NEGATIVE,
        "role_member": EVERYONE_NEGATIVE,
        "role_logs": EVERYONE_EXPLICIT_READ_ONLY,
        "role_detained": EVERYONE_NEGATIVE,
        "role_muted": EVERYONE_NEGATIVE,
        "role_super_muted": EVERYONE_NEGATIVE,
        "role_everyone": EVERYONE_NEGATIVE,
    },
}

LOCKED_OVERWRITE_MAP = {
    "information": {
        "role_warden": GLOBAL_SAFE,
        "role_director": DIRECTOR_READ_ONLY,
        "role_moderator": EVERYONE_READ_ONLY,
        "role_citizen": EVERYONE_READ_ONLY,
        "role_member": EVERYONE_READ_ONLY,
        "role_logs": BASE,
        "role_detained": EVERYONE_READ_ONLY,
        "role_muted": EVERYONE_READ_ONLY,
        "role_super_muted": EVERYONE_NEGATIVE,
        "role_everyone": BASE,
    },
    "verification": {
        "role_warden": GLOBAL_SAFE,
        "role_director": DIRECTOR_BASE,
        "role_moderator": EVERYONE_NEGATIVE,
        "role_citizen": EVERYONE_NEGATIVE,
        "role_member": EVERYONE_NEGATIVE,
        "role_logs": BASE,
        "role_detained": EVERYONE_NEGATIVE,
        "role_muted": EVERYONE_NEGATIVE,
        "role_super_muted": EVERYONE_NEGATIVE,
        "role_everyone": EVERYONE_SEND_ONLY,
    },
    "community_updates": {
        "role_warden": GLOBAL_SAFE,
        "role_director": DIRECTOR_READ_ONLY,
        "role_moderator": EVERYONE_NEGATIVE,
        "role_citizen": EVERYONE_NEGATIVE,
        "role_member": EVERYONE_NEGATIVE,
        "role_logs": BASE,
        "role_detained": EVERYONE_NEGATIVE,
        "role_muted": EVERYONE_NEGATIVE,
        "role_super_muted": EVERYONE_NEGATIVE,
        "role_everyone": EVERYONE_NEGATIVE,
    },
    "moderation": {
        "role_warden": GLOBAL_SAFE,
        "role_director": DIRECTOR_MODERATION,
        "role_moderator": MODERATOR_MODERATION,
        "role_citizen": EVERYONE_NEGATIVE,
        "role_member": EVERYONE_NEGATIVE,
        "role_logs": BASE,
        "role_detained": EVERYONE_NEGATIVE,
        "role_muted": EVERYONE_NEGATIVE,
        "role_super_muted": EVERYONE_NEGATIVE,
        "role_everyone": EVERYONE_NEGATIVE,
    },
    "director_commands": {
        "role_warden": GLOBAL_SAFE,
        "role_director": DIRECTOR_MODERATION,
        "role_moderator": EVERYONE_NEGATIVE,
        "role_citizen": EVERYONE_NEGATIVE,
        "role_member": EVERYONE_NEGATIVE,
        "role_logs": BASE,
        "role_detained": EVERYONE_NEGATIVE,
        "role_muted": EVERYONE_NEGATIVE,
        "role_super_muted": EVERYONE_NEGATIVE,
        "role_everyone": EVERYONE_NEGATIVE,
    },
    "isolation": {
        "role_warden": GLOBAL_SAFE,
        "role_director": DIRECTOR_READ_ONLY,
        "role_moderator": EVERYONE_READ_ONLY,
        "role_citizen": EVERYONE_NEGATIVE,
        "role_member": EVERYONE_NEGATIVE,
        "role_logs": BASE,
        "role_detained": EVERYONE_EXPLICIT_READ_ONLY,
        "role_muted": EVERYONE_NEGATIVE,
        "role_super_muted": EVERYONE_NEGATIVE,
        "role_everyone": EVERYONE_NEGATIVE,
    },
    "interface": {
        "role_warden": GLOBAL_SAFE,
        "role_director": DIRECTOR_READ_ONLY,
        "role_moderator": EVERYONE_READ_ONLY,
        "role_citizen": EVERYONE_READ_ONLY,
        "role_member": EVERYONE_READ_ONLY,
        "role_logs": BASE,
        "role_detained": EVERYONE_NEGATIVE,
        "role_muted": EVERYONE_READ_ONLY,
        "role_super_muted": EVERYONE_NEGATIVE,
        "role_everyone": BASE,
    },
    "commands": {
        "role_warden": GLOBAL_SAFE,
        "role_director": DIRECTOR_BASE,
        "role_moderator": MODERATOR_BASE,
        "role_citizen": EVERYONE_READ_ONLY,
        "role_member": EVERYONE_READ_ONLY,
        "role_logs": EVERYONE_READ_ONLY,
        "role_detained": EVERYONE_NEGATIVE,
        "role_muted": EVERYONE_READ_ONLY,
        "role_super_muted": EVERYONE_NEGATIVE,
        "role_everyone": BASE,
    },
    "community": {
        "role_warden": GLOBAL_SAFE,
        "role_director": DIRECTOR_BASE,
        "role_moderator": MODERATOR_BASE,
        "role_citizen": EVERYONE_READ_ONLY,
        "role_member": EVERYONE_READ_ONLY,
        "role_logs": EVERYONE_READ_ONLY,
        "role_detained": EVERYONE_NEGATIVE,
        "role_muted": EVERYONE_READ_ONLY,
        "role_super_muted": EVERYONE_NEGATIVE,
        "role_everyone": BASE,
    },
    "debate": {
        "role_warden": GLOBAL_SAFE,
        "role_director": EVERYONE_READ_ONLY,
        "role_moderator": EVERYONE_READ_ONLY,
        "role_citizen": EVERYONE_READ_ONLY,
        "role_member": EVERYONE_READ_ONLY,
        "role_logs": EVERYONE_READ_ONLY,
        "role_detained": EVERYONE_NEGATIVE,
        "role_muted": EVERYONE_READ_ONLY,
        "role_super_muted": EVERYONE_NEGATIVE,
        "role_everyone": BASE,
    },
    "debate-#": {
        "role_warden": GLOBAL_SAFE,
        "role_director": EVERYONE_READ_ONLY,
        "role_moderator": EVERYONE_READ_ONLY,
        "role_citizen": EVERYONE_NO_READ,
        "role_member": EVERYONE_NO_READ,
        "role_logs": BASE,
        "role_detained": EVERYONE_NEGATIVE,
        "role_muted": EVERYONE_NEGATIVE,
        "role_super_muted": EVERYONE_NEGATIVE,
        "role_everyone": BASE,
    },
    "logs": {
        "role_warden": GLOBAL_SAFE,
        "role_director": DIRECTOR_LOGS,
        "role_moderator": EVERYONE_NEGATIVE,
        "role_citizen": EVERYONE_NEGATIVE,
        "role_member": EVERYONE_NEGATIVE,
        "role_logs": EVERYONE_EXPLICIT_READ_ONLY,
        "role_detained": EVERYONE_NEGATIVE,
        "role_muted": EVERYONE_NEGATIVE,
        "role_super_muted": EVERYONE_NEGATIVE,
        "role_everyone": EVERYONE_NEGATIVE,
    },
}


def generate_overwrite(ctx, roles, channel: str, locked: bool = False):
    """
    Parameters
    ----------
    ctx: discord context
    roles: a dict of roles pulled from db
    channel: name of any GuildChannel
    locked: whether the overwrite should be locked state of server

    Returns
    -------
    A dict of roles and their overwrites for a specific channel
    """
    if locked:
        overwrites = LOCKED_OVERWRITE_MAP[channel]
    else:
        overwrites = UNLOCKED_OVERWRITE_MAP[channel]
    return {
        roles["role_warden"]: overwrites["role_warden"],
        roles["role_director"]: overwrites["role_director"],
        roles["role_moderator"]: overwrites["role_moderator"],
        roles["role_citizen"]: overwrites["role_citizen"],
        roles["role_member"]: overwrites["role_member"],
        roles["role_logs"]: overwrites["role_logs"],
        roles["role_detained"]: overwrites["role_detained"],
        roles["role_muted"]: overwrites["role_muted"],
        roles["role_super_muted"]: overwrites["role_super_muted"],
        ctx.guild.default_role: overwrites["role_everyone"],
    }
